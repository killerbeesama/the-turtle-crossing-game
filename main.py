from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()


player = Player()
carmanager = CarManager()
scoreboard = ScoreBoard()

screen.onkeypress(player.move,'w')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    carmanager.random_car()
    carmanager.obstacle()
    if player.ycor() > 260:
        scoreboard.update_score()
        player.reset_position()
        carmanager.increase_speed()
    for car in carmanager.cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()