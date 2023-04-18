from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def hop(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)