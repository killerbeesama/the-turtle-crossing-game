from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-280,260) 
        self.level = 0
        self.score()

    
    def score(self):
        self.clear()
        self.write(f"level: {self.level}", align='left', font=('Arial', 25, 'normal'))


    def update_score(self):
        self.level += 1
        self.score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Arial', 25, 'normal'))