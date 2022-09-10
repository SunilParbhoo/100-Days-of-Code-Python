from random import choice
from hangman_words import word_list
from hangman_art import logo, congrats, stages
import os


def clear():
    os.system('clear')


end_of_game = False
chosen_word = choice(word_list)
word_length = len(chosen_word)
lives = 6
guessed = []

print(logo)

# Testing code
print(f"Psst... the solution is {chosen_word}.")

# Create blanks
display = []
for letter in chosen_word:
    display += "_"


while not end_of_game:
    print(f"{' '.join(display)}")
    print(stages[lives])
    # print(lives)
    guess = input("Guess a letter: ").lower()
    clear()

    if guess not in guessed:
        guessed.append(guess)
        if guess in chosen_word:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        elif guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in the word")
            if lives == 0:
                end_of_game = True
                print(stages[lives])
                print("You lose.")
    elif guess in guessed:
        print(f"You've already guessed {guess}")

    if "_" not in display:
        end_of_game = True
        print(f"{' '.join(display)}")
        print(congrats)
        print("You win.")

    # print(hangman_art.stages[lives])
