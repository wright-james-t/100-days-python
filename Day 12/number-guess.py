# To do list:
#
# Greeting the player
#
# Selecting and storing random number between 1-100
#
# Selecting easy or hard difficulty
#
# Storing guess limits based on chosen difficulty
#
# Storing user guess
#
# Determining if the guess is higher, lower, or equal to the randomly chosen number
# If != to chosen number, deduct one life and if lives <= 0, call them a loser
# If lives > 0, tell them if the number was higher or lower and restart the prompt with an update life total

# Importing modules and declaring vars
import random

easyAttempts = 10
hardAttempts = 5
attempts = 0
gameOver = False
randomNumber = 0

# Defining necessary functions

# to be called whenever the user guesses incorrectly
def decrementAttempts():
    global attempts
    attempts -= 1
    return attempts

# to be called whenever we need to check if the user has lost or won
def gameOverCheck(userGuess = 0):
    global gameOver
    if attempts <= 0:
        print(f"The number was {randomNumber}, you ran out of attempts. You lose.")
        gameOver = True
        playAgain()
    elif userGuess == randomNumber:
        print(f"You got it, you win!")
        gameOver = True
        playAgain()

# to be called to check if the user wants to play again after winning/losing
def playAgain():
    global gameOver
    again = input(f"Would you like to play again? [y,n]: ")
    if again == 'y' or again == 'Y':
        gameOver = False
        gameSetup()
    else:
        print(f"Maybe next time!")

# to be called whenever we need to check if the users guess was high, low, or correct
def guessCheck(userGuess):
    if userGuess > randomNumber:
        print("Too high!")
        decrementAttempts()
        gameOverCheck()
    elif userGuess < randomNumber:
        print("Too low!")
        decrementAttempts()
        gameOverCheck()
    else:
        gameOverCheck(userGuess)

# welcome prompt + choosing new number
def gameSetup():
    global attempts
    global randomNumber
    global gameOver
    randomNumber = random.choice(range(1, 100))
    print(f"Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\n")
    chosenDifficulty = input(f"What difficulty would you like to play on? Type 'easy' or 'hard': ")
    if chosenDifficulty == 'easy':
        attempts = easyAttempts
    elif chosenDifficulty == 'hard':
        attempts = hardAttempts
    else:
        print(f"\"{chosenDifficulty}\" is not an option, you lose.")
        gameOver = True
    # Select/store number between 1-100

# Greeting and initial set up
gameSetup()


# The game is afoot
while not gameOver:
    print(f"You have {attempts} attempts remaining.\n")
    guessCheck(int(input(f"Make a guess: ")))
