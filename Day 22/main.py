from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

# Screen set up
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Scoreboard set up
scoreboard = Scoreboard()

# Right Paddle creation
right_paddle = Paddle((350, 0))

# Left Paddle creation
left_paddle = Paddle((-350, 0))

# Paddle Control setup
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# Ball creation
ball = Ball()


# The game is afoot
game_is_on = True
while game_is_on:
    ball.move()
    dir_change = [1, 2]
    rand_choice = random.choice(dir_change)
    # Detect wall collision
    if ball.ycor() >= 280:
        ball.bounce_y()
    elif ball.ycor() <= -280:
        ball.bounce_y()

    # Detect Paddle Collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.speed_increase()
        ball.bounce_x()

    # Detect Scoring
    if ball.xcor() > 370:
        scoreboard.increase_score("left")
        scoreboard.update_score()
        ball.reset()
        ball.bounce_x()
        if rand_choice == 1:
            ball.bounce_y()

    if ball.xcor() < -370:
        scoreboard.increase_score("right")
        scoreboard.update_score()
        ball.reset()
        ball.bounce_x()
        if rand_choice == 1:
            ball.bounce_y()

    screen.update()
    time.sleep(ball.move_speed)

screen.exitonclick()
