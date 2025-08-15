import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_hand = []
user_hand = []
ace = 11


print(art.logo)

def draw_card():
    new_card = random.choice(cards)
    user_hand.append(new_card)
    return new_card

def computer_draw_card():
    new_card = random.choice(cards)
    computer_hand.append(new_card)
    return new_card

# def update_score():
   # for card in user_hand:
     #   user_score = user_hand[card]

new_game = input("Do you want to play a game of Blackjack type 'y' or 'n': ")
if new_game.lower() == "n":
    game_over = True

else:
    game_over = False

    usr_card1 = draw_card()
    usr_card2 = draw_card()
    usr_score = usr_card1 + usr_card2

    cpu_card1 = computer_draw_card()
    cpu_card2 = computer_draw_card()
    cpu_score = cpu_card1 + cpu_card2

    if cpu_score == 21 or usr_score == 21 and cpu_score == 21:
        print("Computer got blackjack, you lose. :(")
        game_over = True

    elif usr_score == 21:
        print("Blackjack, you win!")
        game_over = True

    if usr_score > 21:
        print("Score over 21, you lose. :(")
        game_over = True

    print("Your cards:" + str(user_hand) + ", current score: " + str(usr_score))
    print("Computer's first card: " + str(cpu_card1))

    while not game_over:
        draw = input("Type 'y' to draw a card, type 'n' to pass: ")
        if draw.lower() == "y":
            usr_card3 = draw_card()
            usr_score += usr_card3

            if usr_score > 21:
                print("Score over 21, you lose. :(")
                game_over = True
        else:
            if cpu_score < 16:
                cpu_card3 = computer_draw_card()
                cpu_score += cpu_card3

        if usr_score < cpu_score:
            print("Computer has higher score, you lose")
            game_over = True
        elif usr_score > cpu_score:
            print("You have higher score, you win")
            game_over = True
        else:
            print("Its a tie. :P")
            game_over = True

        print("Your cards:" + str(user_hand) + ", current score: " + str(usr_score))
        print("Computer's final hand: " + str(computer_hand) + ", final score: " + str(cpu_score))
