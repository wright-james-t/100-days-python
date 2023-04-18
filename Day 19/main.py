from turtle import *
import turtle
from random import *
import random

screen = Screen()
screen.setup(width=1000, height=1000)
userBet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']

isOn = False
allTurtles = []


def createTurtles():
    xPoint = -400
    yPoint = -300
    for num in range(len(colors)):
        turtleName = Turtle(shape="turtle")
        allTurtles.append(turtleName)
        turtleName.color(colors[num])
        turtleName.penup()
        turtleName.goto(xPoint, yPoint)
        yPoint += 100


if userBet:
    isOn = True

createTurtles()

while isOn:
    for raceTurtle in allTurtles:
        moveDistance = random.randint(1, 10)
        raceTurtle.forward(moveDistance)
        if raceTurtle.xcor() > 480:
            winning_color = raceTurtle.pencolor()
            isOn = False

if userBet == winning_color:
    print(f"You've won! The {winning_color} turtle has won the race!")
else:
    print(
        f"You've lost! The {winning_color} turtle won the race, but you chose the {userBet} turtle.")

turtle.mainloop()