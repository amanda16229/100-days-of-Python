import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = 6

chosenWord = random.choice(hangman_words.word_list)
# print(chosenWord) omitted so player cannot see chosen word

correct_letters = []
all_guesses = []
placeholder = ""

for letter in chosenWord:
    placeholder += "_"

print("Chosen word: " + placeholder)

gameOver = False
while not gameOver:
    print(f'{lives} lives left.')

    display = "" # every time we make a guess the display changes so it must always start off as blank and be built from there

    guess = input("Enter a letter: ")
    all_guesses.append(guess)

    if guess in correct_letters:
        print(guess + " has already been guessed.")

    for letter in chosenWord:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"    

    print(display)
    print(all_guesses)

    if guess not in chosenWord:
        print(guess + " is not in chosen word. You lose 1 life.")
        lives -= 1

    if lives == 0:
        gameOver = True
        print("You lose. Chosen word was: " + chosenWord)

    if "_" not in display:
        gameOver = True
        print("You win!")

    print(hangman_art.stages[lives])