from snake_body import Snake
from food import Food
from turtle import Screen,Turtle
from score import Snakescore
from loss import Loss
from road_block import Block
import time


window = Screen()
window.setup(width=800,height=800)
window.setup(width=1.0,height=1.0)
window.bgcolor("black")
window.title("Null")
window.tracer(0)
block = Block()
block.draw_block()
food = Food()
losing = Loss()
score = Snakescore()
my_snake = Snake()
game_on = True
while game_on:
    window.update()
    my_snake.manual()
    time.sleep(0.1)
    window.listen()
    window.onkey(my_snake.up,"w")
    window.onkey(my_snake.left,"a")
    window.onkey(my_snake.right,"d")
    window.onkey(my_snake.down,"s")
    if my_snake.snake_head.distance(food) < 15:
        score.add_score()
        food.randplace()
        my_snake.extension()
    if my_snake.snake_head.xcor() > 598 or my_snake.snake_head.xcor() < -600 or my_snake.snake_head.ycor() > 360 or my_snake.snake_head.ycor() < -330:
        window.bgcolor(losing.bgcolor)
        losing.wrtie_lose(score.score)
        break
    for x in my_snake.turtle:
        if x != my_snake.snake_head:
            if x.pos() == my_snake.snake_head.pos():
                window.bgcolor(losing.bgcolor)
                losing.wrtie_lose(score.score)
                game_on = False
window.exitonclick()