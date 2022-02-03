from turtle import Turtle
import random

COLORS = ['red','orange','yellow','green','blue','purple']

class CarManager:

    def __init__(self) -> None:
        self.cars = []
        self.move_speed = 5
        
        
    def random_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            t = Turtle('square')
            t.penup()
            t.shapesize(stretch_wid=1,stretch_len=2)
            t.color(random.choice(COLORS))
            t.goto(280,random.randint(-200,200))
            self.cars.append(t)


    def obstacle(self):
        for i in self.cars:
            i.backward(self.move_speed)

    
    def increase_speed(self):
        self.move_speed += 10