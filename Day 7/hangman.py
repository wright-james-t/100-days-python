# Flow Chart:
#
# Generate and store random word
#
# Generate "blanks" for each letter in the word
#
# Prompt the user to guess a letter
#
# On a correct guess, fill in the letter in the appropriate "blank"
# or on an incorrect guess, add the letter to an "incorrect" guesses area and draw a piece
#
# Check the state of the game (pass, fail, or continue) and respond accordingly
import random

# Step 1

# word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# myWord = random.choice(word_list)
#
# userGuess = input("What letter would you like to guess?\n").lower()
#
# letters = [*myWord]
#
# for num in range(0, len(letters)):
#     if userGuess == letters[num]:
#         print(f"Value is: {letters[num]}, correct guess")
#     else:
#         print(f"Value is: {letters[num]}, wrong guess")

# Step 2

# Testing code

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# print(f"The word is: {myWord}")
#
# display = []
#
# for char in letters:
#     display.append("_")
#
# print(display)
#
# print(f"Adding your letters if applicable")
#
# for num in range(0, len(letters)):
#     if userGuess == letters[num]:
#         display[num] = userGuess
#
# print(display)

gameOver = False
word_list = ["aardvark", "baboon", "camel"]
myWord = random.choice(word_list)
letters = [*myWord]
display = []
for char in letters:
    display.append("_")

while not gameOver:
    remainingLetters = int(len(letters))
    print(display)
    userGuess = input("What letter would you like to guess?\n").lower()
    for num in range(0, len(letters)):
        if userGuess == letters[num]:
            display[num] = userGuess
            blank = False
    for check in display:
        # Could have used if "_" not in ${list} instead of jank variable decrementing
        if check != '_':
            remainingLetters -= 1
            if remainingLetters == 0:
                print("You win!")
                gameOver = True
