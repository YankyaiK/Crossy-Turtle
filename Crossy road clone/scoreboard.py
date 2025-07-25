FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.goto(-270,-270)
        self.write(self.score, align= "center", font=FONT)
    def point(self):
        self.clear()
        self.score += 1
        self.update_score()


    def fail(self):
        self.goto(0,0)
        self.write("Game Over", align= 'center', font= FONT)