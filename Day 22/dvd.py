from turtle import Turtle

class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen.register_shape("dvd", "logo.png")
        self.shape("dvd")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        ball_x = self.xcor() + self.x_move
        ball_y = self.ycor() + self.y_move
        self.goto(ball_x, ball_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def speed_increase(self):
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1