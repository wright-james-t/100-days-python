import random

cards = {
    "Ace": 11,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    10: 10,
    9: 9,
    8: 8,
    7: 7,
    6: 6,
    5: 5,
    4: 4,
    3: 3,
    2: 2
}

dealerHand = []
dealerHandValue = 0

playerHand = []
playerHandValue = 0

gameOver = False


def drawCard(target):
    drawnCard = random.choice(list(cards.keys()))
    target.append(drawnCard)


def updateDealerHandValue():
    global dealerHandValue
    dealerHandValue = 0
    for card in dealerHand:
        dealerHandValue += cards[card]
    if dealerHandValue > 21:
        cards.update({"Ace": 1})
        dealerHandValue = 0
        for card in dealerHand:
            dealerHandValue += cards[card]
        cards.update({"Ace": 11})

def updatePlayerHandValue():
    global playerHandValue
    playerHandValue = 0
    for card in playerHand:
        playerHandValue += cards[card]
    if playerHandValue > 21:
        cards.update({"Ace": 1})
        playerHandValue = 0
        for card in playerHand:
            playerHandValue += cards[card]
        cards.update({"Ace": 11})

def dealerLogic():
    global dealerHandValue
    while dealerHandValue < 17:
        drawCard(dealerHand)
        updateDealerHandValue()
    print(f"Dealer final hand: {dealerHand}, Dealer final value: {dealerHandValue}\nPlayer final hand: {playerHand}, Player final value: {playerHandValue}")
    if dealerHandValue > 21:
        print("You win!")
    elif dealerHandValue >= playerHandValue:
        print(f"You lose!")
    else:
        print("You win!")

def gameSetup():
    gameStart = str(input("Placeholder Logo\n\nDo you want to play a game of blackjack? [y,n]\n"))
    if gameStart == 'y' or gameStart == 'Y':
        drawCard(playerHand)
        drawCard(playerHand)
        drawCard(dealerHand)
        updatePlayerHandValue()
        updateDealerHandValue()
    else:
        print("Maybe next time!")
        global gameOver
        gameOver = True


gameSetup()

while not gameOver:
    print(f"Your current hand:\n{playerHand}\nCurrent total: {playerHandValue}\n\n")
    print(f"Dealer Hand:\n{dealerHand}\nCurrent Total: {dealerHandValue}\n\n")
    userAnswer = input("Would you like to hit? [y,n]\n")
    if userAnswer == 'y' or userAnswer == 'Y':
        drawCard(playerHand)
        updatePlayerHandValue()
        print(f"New Hand is: {playerHand}")
        if playerHandValue > 21:
            print(f"Your final hand: {playerHand}, value: {playerHandValue}, you busted!")
            gameOver = True
    elif userAnswer == 'n' or userAnswer == 'N':
        dealerLogic()
        gameOver = True
    else:
        print("That is not a valid input")
        gameOver = True
