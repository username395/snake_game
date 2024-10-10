from turtle import Turtle
class Snakescore(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,300)
        self.pendown()
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score {self.score}",align="center",font=("Arial",20,"normal"))
    def add_score(self):
        self.score += 1
        self.update_score()