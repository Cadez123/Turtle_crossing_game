import turtle
from turtle import Turtle, Screen
from car import Car
import time
import random
from player import Player
from level import Level

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

# player setup
player = Player()
screen.onkey(player.move_up,'w')
screen.onkey(player.move_down,'s')

# car list
car_list = []
level = Level()

# game variables
game_on = True
add_car = 0
sleep_time = 0.1

# game loop
while game_on:
    screen.update()
    time.sleep(sleep_time)
    # generate cars every 5 integrations
    if add_car % 5 == 0:
        for x in range(random.randint(0,2)):
            car = Car()
            car_list.append(car)

    # move each car and delete them after
    for car in car_list:
        car.move_forward()
        if car.xcor() < -220:
            car_list.remove(car)
            car.reset()
            car.hideturtle()

        # check collision
        if car.distance(player) < 20:
            print('game over')
            level.game_over()
            game_on = False
    # if player reaches the end, restart at bottom and make cars faster
    if player.ycor() > 280:
        player.goto(-30,-280)
        sleep_time *= 0.8
        level.level_up()

    add_car += 1


screen.exitonclick()