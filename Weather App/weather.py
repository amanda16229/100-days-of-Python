import tkinter as tk
import requests


API_KEY = '<api_key>'
ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'

window = tk.Tk()
window.title('Weather Alert App')
tk.Label(window, text="Tampa FL weather: ").pack() # using tampa latitude & longitude


# dictionary - must follow the keys provided in API docs
weather_params = {
    "lat": 27.9,
    "lon": 82.4,
    "appid": API_KEY,
    "cnt": 4, # (optional) - only uses next 4 entries of weather data
}

# want to make our GET requests to the endpoint - check the data they already have, get it
# provide params = want type of data we get back (in this case its weather info)
response = requests.get(ENDPOINT, params=weather_params)

weather_data = response.json()

will_rain = False

for data in weather_data['list']:
    temp_k = data['main']['feels_like']
    temp_f = ((temp_k - 273.15) * 1.8) + 32
    formatted_temp_f = '%.1f' % temp_f
    print(formatted_temp_f)
    tk.Label(window, text=formatted_temp_f).pack()

for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) != 700:
        will_rain = True
        tk.Label(window, text="Its gonna rain!").pack()


window.mainloop()
