from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.active_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2.5)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.active_cars.append(new_car)

    def drive(self):
        for car in self.active_cars:
            car.forward(self.car_speed)

    def car_cleanup(self):
        for car in self.active_cars:
            if car.xcor() <= -300:
                car.ht()
                del self.active_cars[0]

    def car_vroom(self):
        self.car_speed += MOVE_INCREMENT
