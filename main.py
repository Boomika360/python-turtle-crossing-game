import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.move_turtle,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
     #detect collisions with cars
    for car in car_manager.all_cars:
        if car.distance(player)<30:
            game_is_on=False
            scoreboard.game_over()
    #detect if the turtle reached the top
    if player.ycor()>280:
        player.reset_original()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()