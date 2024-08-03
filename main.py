from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


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

    #detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        



















screen.exitonclick()

