import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

sleep_time = 0.1

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Frogger")
screen.tracer(0)

# Turtle setup
player = Player()

# Control setup
screen.listen()
screen.onkeypress(player.hop, "Up")

# Car Setup
car_manager = CarManager()

# Scoreboard setup
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    car_manager.create_car()
    car_manager.drive()
    car_manager.car_cleanup()
    for car in car_manager.active_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 280:
        scoreboard.update_level()
        car_manager.car_vroom()
        player.reset_position()

screen.exitonclick()