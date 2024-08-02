from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down,'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



















screen.exitonclick()

