from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self_x = 0
        self_y = 0

    def add_state_to_map(self, state_name, state_x, state_y):
        self.goto(state_x, state_y)
        self.write(state_name)