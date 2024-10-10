from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5,0.5)
        self.randplace()
    def randplace(self):
        random_x = randint(-255,255)
        random_y = randint(-255,255)
        self.goto(random_x,random_y)