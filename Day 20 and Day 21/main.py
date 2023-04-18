from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# screen set up
screen = Screen()

# set up Scoreboard
scoreboard = Scoreboard()

# 600 px by 600 px
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("I lost the game")
screen.tracer(0)
screen.listen()

# Create Snake
snake = Snake()
food = Food()

# Set up keyboard controls
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# The game is afoot
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect food collision
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

# Detect wall collision
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()


# Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()
