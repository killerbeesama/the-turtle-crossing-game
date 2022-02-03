from turtle import Turtle

class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('white')
        self.left(90)
        self.reset_position()


    def reset_position(self):
        self.goto(0,-280)


    def move(self):
        self.forward(20)