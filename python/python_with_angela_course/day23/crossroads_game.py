import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(tim.up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    
    for car in car_manager.all_cars:
        if tim.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if tim.complete_level() == True:
        tim.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

    


screen.exitonclick()