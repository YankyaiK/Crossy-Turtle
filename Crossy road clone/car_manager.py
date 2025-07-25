COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speeder = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_car =Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(1, 2)
            new_car.goto(320, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speeder)

    def level_up(self):
        self.speeder += MOVE_INCREMENT


