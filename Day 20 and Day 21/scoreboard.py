from turtle import Turtle

SCORE_POSITION = (-250, 270)
HIGH_SCORE_POSITION = (220, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("highscore.txt", mode="r") as file:
            self.hsfile = int(file.read())
        self.high_score = self.hsfile
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f"Score: {self.score}", align="center", font=("Comic Sans", 15, "normal"))
        self.goto(HIGH_SCORE_POSITION)
        self.write(f"High Score: {self.high_score}", align="center", font=("Comic Sans", 15, "normal"))


    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"Game Over!", align="center", font=("Comic Sans", 25, "normal"))
    #     self.goto(0,-30)
    #     self.write(f"Your final score was: {self.score}", align="center", font=("Comic Sans", 25, "normal"))
