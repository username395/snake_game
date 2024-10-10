from turtle import Turtle
class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,370)
        self.left(90)
        self.pendown()
    def draw_block(self):
        self.left(90)
        self.forward(600)
        self.left(90)
        self.forward(700)
        self.left(90)
        self.forward(1200)
        self.left(90)
        self.forward(700)
        self.left(90)
        self.forward(600)
