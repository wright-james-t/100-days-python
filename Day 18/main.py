from turtle import Turtle
from turtle import Screen
from random import randint
from random import random
from random import choice
import random
import turtle as t
import colorgram
# from colorgram import *


donatello = Turtle()
donatello.shape("turtle")
donatello.speed(0)

# each side length of 100
# each shape a random color

""" sideCount = 3

while sideCount < 11:
    angleDegree = 360 / sideCount
    penColor = random(), random(), random()
    for i in range(sideCount):
        donatello.forward(100)
        donatello.right(angleDegree)
    sideCount += 1
    donatello.pencolor(penColor) """

donatello.pensize(2)
# randomChoice = ['left', 'right', 'forward']
t.colormode(255)
# is_walking = True


""" def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b """


""" while is_walking:
    choice = random.choice(randomChoice)
    donatello.pencolor(randomColor())
    donatello.color(randomColor())
    if choice == 'forward':
        donatello.forward(10)
    elif choice == 'left':
        donatello.left(90)
        donatello.forward(10)
    else:
        donatello.right(90)
        donatello.forward(10) """

""" degreeCount = 0
while degreeCount < 360:
    donatello.circle(100, None, None)
    degreeCount += 5
    donatello.setheading(degreeCount)
    donatello.pencolor(randomColor()) """

# 10x10 square, circles 20, 50 apart

extractedColors = colorgram.extract('galaxy.jpg', 30)

colorPallette = []

for i in range(len(extractedColors)):
    color = extractedColors[i]
    colorPallette.append(tuple((color.rgb.r, color.rgb.b, color.rgb.g)))
# print(colorPallette[randomColor])

""" for i in range(10):
    for i in range(10):
        randomIndex = random.randint(0, len(colorPallette) - 1)
        randomColor = colorPallette[randomIndex]
        donatello.pencolor(randomColor)
        donatello.fillcolor(randomColor)
        donatello.begin_fill()
        donatello.circle(10)
        donatello.end_fill()
        donatello.penup()
        donatello.forward(50)
        donatello.pendown()
    donatello.penup()
    yCoordinate += 50
    donatello.setpos(0, yCoordinate)
    donatello.pendown() """

donatello.penup()
donatello.setpos(-500, -500)
donatello.hideturtle()
yCoordinate = -500

for i in range(10):
    for i in range(10):
        randomIndex = random.randint(0, len(colorPallette) - 1)
        randomColor = colorPallette[randomIndex]
        donatello.dot(20, randomColor)
        donatello.forward(50)
    yCoordinate += 50
    donatello.setpos(-500, yCoordinate)

screen = t.Screen()
screen.exitonclick()