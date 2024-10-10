from turtle import Turtle
class Loss(Turtle):
    def __init__(self):
        super().__init__()
        self.bgcolor = "dark red"
        self.hideturtle()
        self.color("white")
        self.goto(0,0)
    def wrtie_lose(self,score):
        self.write(f"Game Over!\nFinal Score: {score}",align="center",font=("Arial",20,"normal"))