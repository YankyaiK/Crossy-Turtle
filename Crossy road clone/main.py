import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()

car = CarManager()

screen.onkey(fun=turtle.move, key= "Up")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move_car()
    if turtle.finish():
        turtle.goto(player.STARTING_POSITION)
        car.level_up()
        score.point()



    for cars in car.all_cars:
        if turtle.distance(cars) < 10:
            game_is_on =False
            score.fail()


screen.exitonclick()