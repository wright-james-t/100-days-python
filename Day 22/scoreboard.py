from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.left_score, align="center", font=("Comic Sans", 50, "normal"))
        self.goto(200, 200)
        self.write(self.right_score, align="center", font=("Comic Sans", 50, "normal"))


    def increase_score(self, position):
        if position == "left":
            self.left_score += 1
            self.update_score()
        elif position == "right":
            self.right_score +=1
            self.update_score()


