# To do:
# Import art/data from provided files
# (name, follower_count, description, country)
#
# Choose a random set of people from the dictionary
#
# Assign them to A/B
#
# Write a function to compare the follower_count of person a to b
#
# Write a function to increment score
#
# Write a game setup function
#
# Write a play again function
#
# write the while loop for the game which prompts the user for a choice and then uses the above
# functions to compare and let the user know if they were right or wrong
#   if wrong, game over screen with score displayed
#   if right, "correct" answer becomes new "A" choice and a new "B" choice is randomly chosen, start loop over


# Import stuff from secondary files and the random library

import random
import os
from game_data import data
from art import logo, vs

# define necessary vars and functions
def randomPerson():
    """Returns a random person from the data set"""
    return random.choice(data)


def getGuess(choiceA, choiceB):
    """Asks the user for their guess and returns it"""
    guess = ""
    while guess not in ['A', 'B', 'a', 'b']:
        guess = input(f"Choice A: {choiceA['name']}, a {choiceA['description']} from {choiceA['country']}\n{vs}\nChoice B: {choiceB['name']}, a {choiceB['description']} from {choiceB['country']}\n\nWho do you think has a higher follower count? [A, B]")
    return guess


def thugAim():
    """The game is afoot"""
    score = 0
    gameOver = False
    keepA = False
    while not gameOver:
        if keepA == False:
            choiceA = randomPerson()
            choiceB = randomPerson()
        else:
            choiceA = choiceB
            choiceB = randomPerson()

        userGuess = getGuess(choiceA, choiceB)

        if choiceA['follower_count'] > choiceB['follower_count']:
            correctAnswer = 'A'
        else:
            correctAnswer = 'B'

        if userGuess == correctAnswer:
            score += 1
            os.system('cls')
            print(f"You're right! Current score: {score}")
            if correctAnswer == 'B':
                keepA = True
        else:
            print(f"Game over!. Final score is {score}.")
            playAgain = ""
            while playAgain not in ['y', 'n', 'Y', 'N']:
                playAgain = input("Do you want to play again? [y,n]: ")
            if playAgain == 'y' or playAgain == 'Y':
                gameOver = False
            else:
                print("Maybe next time!")
                gameOver = True

print(logo)
thugAim()