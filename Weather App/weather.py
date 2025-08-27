import tkinter as tk
import requests


API_KEY = '<api_key>'
ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'

def get_entry(event):
    zip_code = search_var.get()
    print("Zip code: ", zip_code)

    # dictionary - must follow the keys provided in API docs
    weather_params = {
        "zip": zip_code,
        "appid": API_KEY,
        "cnt": 4,  # (optional) - only uses next 4 entries of weather data
    }

    # want to make our GET requests to the endpoint - check the data they already have, get it
    # provide params = want type of data we get back (in this case its weather info)

    response = requests.get(ENDPOINT, params=weather_params) # request sent to api (returns number code)

    weather_data = response.json()

    if weather_data.get("cod") != "200":
        print("Error fetching weather forecast: ", weather_data.get("message"))
        
    else:
        print("Success! Here is your forecast: ")

    print(weather_data)
    print("Response code: " + str(response))



    tk.Label(window, text=weather_data['list'][0]['main']).pack() # TODO: hard to read list of weather data, json format

    is_raining(weather_data)


def is_raining(weather_data):
    will_rain = False
    i = 0

    for data in weather_data['list']:
        i += 1
        temp_k = data['main']['feels_like']
        temp_f = ((temp_k - 273.15) * 1.8) + 32
        formatted_temp_f = '%.1f' % temp_f
        print(formatted_temp_f)
        tk.Label(window, text="hour (" + str(i) + ")  feels like: " + formatted_temp_f).pack()

    for hour_data in weather_data['list']:
        condition_code = hour_data['weather'][0]['id']
    if int(condition_code) != 700:
        will_rain = True
        tk.Label(window, text="Its gonna rain!").pack()


window = tk.Tk()
window.title('Weather Alert App')

tk.Label(window, text="Search a city for its weather (enter zip code): ").pack() # using tampa latitude & longitude

search_var = tk.StringVar() # holds value of string we will be searching for

search_entry = tk.Entry(window, textvariable=search_var) # adds tkinter search box, grabs entered text & attaches to var
search_entry.pack()

button = tk.Button(window, text="Search")
button.pack()

search_entry.bind('<Return>', get_entry)



window.mainloop()
