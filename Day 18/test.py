from turtle import Turtle
from turtle import Screen
import random

donatello = Turtle()
donatello.shape("turtle")
donatello.speed(0)

sideCount = 3

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

while sideCount < 11:
    angleDegree = 360 / sideCount
#    penColor = 255, 255, 255
    for i in range(sideCount):
        donatello.forward(100)
        donatello.right(angleDegree)
    sideCount += 1
#    donatello.pencolor(penColor)

#screen = Turtle().Screen()
screen.exitonclick()

