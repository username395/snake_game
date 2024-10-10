from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtle = []
        self.position = ((-40,0),(-20,0),(0,0))
        self.create_obj()
        self.snake_head = self.turtle[-1]
    def create_obj(self):
        for x in range(len(self.position)):
            new_obj = Turtle()
            new_obj.shape("square")
            new_obj.penup()
            new_obj.color("white")
            new_obj.goto(self.position[x])
            self.turtle.append(new_obj)
    def manual(self):
        for x in range(len(self.turtle) - 1):
            self.turtle[x].goto(self.turtle[x + 1].pos())
        self.snake_head.forward(20)
    def extension(self):
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(self.turtle[0].pos())
        self.turtle.insert(0,new_snake)
    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)
    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)
    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)