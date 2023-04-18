from turtle import Turtle, Screen
import time

# Screen set up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Pong")
screen.tracer(0)

# Turtle creation
ball = Turtle()


# Ball creation
def create_ball():
    screen.addshape("logo.gif")
    ball.shape("logo.gif")
    ball.penup()
    ball.x_move = 10
    ball.y_move = 10
    ball.move_speed = 0.1
    ball.shapesize(stretch_wid=0.25, stretch_len=0.25)


def move():
    ball_x = ball.xcor() + 10
    ball_y = ball.ycor() + 10
    ball.goto(ball_x, ball_y)


def bounce_y():
    ball.y_move *= -1


def bounce_x():
    ball.x_move *= -1


def speed_increase():
    ball.move_speed *= 0.9


def reset():
    ball.goto(0, 0)
    ball.move_speed = 0.1


create_ball()

# The game is afoot
game_is_on = True
while game_is_on:
    move()
    # Detect wall collision
    if ball.ycor() >= 280:
        bounce_y()
    elif ball.ycor() <= -280:
        bounce_y()
    if ball.xcor() >= 380:
        bounce_x()
    elif ball.xcor() <= -380:
        bounce_x()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()