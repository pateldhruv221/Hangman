
# Hangman Game
# Created by: Dhruv N. Patel (2021)

from random import randint

# DETERMINING LENGTH OF FILE
num_words = 0
with open("words_file.txt", "r") as words_file:
    for word in words_file:
        num_words += 1

def print_hangman():
    print("  _____")
    print(" |     |")
    if wrong_guesses_left == 7:
        print("       |")
        print("       |")
        print("       |")
        print("       |")
    elif wrong_guesses_left == 6:
        print(" O     |")
        print("       |")
        print("       |")
        print("       |")
    elif wrong_guesses_left == 5:
        print(" O     |")
        print(" |     |")
        print("       |")
        print("       |")
    elif wrong_guesses_left == 4:
        print(" O     |")
        print(" |     |")
        print(" |     |")
        print("       |")
    elif wrong_guesses_left == 3:
        print(" O     |")
        print("\|     |")
        print(" |     |")
        print("       |")
    elif wrong_guesses_left == 2:
        print(" O     |")
        print("\|/    |")
        print(" |     |")
        print("       |")
    elif wrong_guesses_left == 1:
        print(" O     |")
        print("\|/    |")
        print(" |     |")
        print("/      |")
    elif wrong_guesses_left == 0:
        print(" O     |")
        print("\|/    |")
        print(" |     |")
        print("/ \    |")

    print("       |")
    print("     -----")

def print_user_progress():
    for letter in user_progress:
        print(f" {letter} ", end="")
    print()

play_again = True

while play_again:

    # EXTRACTING A RANDOM WORD FROM THE FILE
    answer = ""
    rand_index = randint(0, num_words-1)
    with open("words_file.txt", "r") as words_file:
        for i, word in enumerate(words_file):
            if i == rand_index:
                answer = word.strip() #removing new-line character at the end
                break

    # NECESSARY VARIABLES AND FUNCTIONS
    user_progress = "_"*len(answer)
    user_guess = ''
    wrong_guesses_left = 7
    wrong_letters_guessed = []
    right_answer_indices = []

    # INTRO
    print(f"WELCOME TO HANGMAN!\nYou have to guess a {len(answer)}-letter word\n")

    # ---------------------------------------------- GAMEPLAY ----------------------------------------------------

    # main loop
    while user_progress != answer and wrong_guesses_left != 0:
        # display game progress and info
        print_hangman()
        print_user_progress()
        print(f"You have {wrong_guesses_left} wrong guesses left!")
        print(f"Wrong letters guessed: {wrong_letters_guessed}")
        user_guess = input("Enter letter: ").lower()

        while len(user_guess) != 1 or user_guess not in "abcdefghijklmnopqrstuvwxyz":
            print("You have entered input that is either not of the correct length or is not a letter. Please try again")
            user_guess = input("Enter letter: ").lower()

        # Evaluate user guess
        if user_guess in answer:
            #Check to see if user has guessed this right letter before or not
            if user_guess in user_progress:
                print("You have already guessed this right letter! Try again")
            else:
                # Find our where in the answer the letter is
                for i, letter in enumerate(answer):
                    if letter == user_guess:
                        right_answer_indices.append(i)
                # Replace the appropriate places in the user progress
                for i in right_answer_indices:
                    user_progress = user_progress[:i] + user_guess + user_progress[i+1:]
        else:
            #Check to see if user has guessed this wrong letter before or not
            if user_guess in wrong_letters_guessed:
                print("You have already guessed this wrong letter! Try again")
            else:
                wrong_letters_guessed.append(user_guess)
                wrong_guesses_left -= 1

        # Resetting appropriate variables
        right_answer_indices = []

        print() #formatting

    # OUTRO
    if user_progress == answer:
        print("\nCONGRATULATIONS YOU HAVE WON!")
    else:
        print_hangman()
        print("\nYou ran out of tries :(")

    print(f"The answer was {answer}\n")

    play_again_response = input("Would you like to play again? (y/n): ").lower()
    play_again = True if play_again_response == "y" else False
    print()

print("Thank you for playing!")
print("Game created by DNP")
