from turtle import Turtle
from car_manager import CarManager


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-225, 265)
        self.color("Black")
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over!", align="center", font=FONT)
        self.goto(0, -50)
        self.write(f"You made it to level {self.level}!", align="center", font=FONT)