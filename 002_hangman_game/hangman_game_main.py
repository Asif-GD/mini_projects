# credit - Day 7 - 100 Days of Code: The Complete Python Pro Bootcamp
# https://www.udemy.com/course/100-days-of-code/

# flowchat - https://whimsical.com/hangman-XHXMXHCow7vNACR87MXXtF

import random
from hangman_words import word_list
from hangman_art import game_stage, logo

random_word = random.choice(word_list)
print(logo)

# Testing code
print(f'Pssst, the solution is {random_word}.')

# filling random word with blanks
blank_random_word = "_" * len(random_word)
print(f"Your random word is: {blank_random_word}")

end_of_game: [bool] = False
user_lives: [int] = 6
user_guess: [list] = []
while not end_of_game:
    user_guess += input("Guess a letter: ").lower()
    last_guess: [str] = user_guess[len(user_guess) - 1]

    # user has entered a letter they've already guessed, letting them know.
    if user_guess.count(last_guess) > 1:
        print(f"You have already guessed {last_guess}. Try again.")

    # user loses a life for incorrect guess
    elif last_guess not in random_word:
        user_lives -= 1
        print(f"{last_guess} is not in the word. You lose a life.")

    # filling in the guessed letter
    else:
        temp_string: [str] = ""
        for char in random_word:
            if char in user_guess:
                temp_string += char
            else:
                temp_string += "_"

        blank_random_word = temp_string

    # drawing ASCII art of the hangman stage
    print(game_stage[user_lives])

    print(f"Your random word is: {blank_random_word}")
    print(f"Your guesses so far: {user_guess}")
    print(f"Lives left: {user_lives}")

    # checking end-game conditions
    if "_" not in blank_random_word:
        end_of_game = True
        print("You Win. Yaay!")
    elif user_lives == 0:
        end_of_game = True
        print("You Lose. Better luck next time.")
