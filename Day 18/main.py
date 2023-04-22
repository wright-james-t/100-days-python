from turtle import Turtle
from turtle import Screen
from random import randint
from random import random
from random import choice
import random
import turtle as t
import colorgram

donatello = Turtle()
donatello.shape("turtle")
donatello.speed(0)


donatello.pensize(2)
t.colormode(255)

extractedColors = colorgram.extract('galaxy.jpg', 30)

colorPallette = []

for i in range(len(extractedColors)):
    color = extractedColors[i]
    colorPallette.append(tuple((color.rgb.r, color.rgb.b, color.rgb.g)))

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