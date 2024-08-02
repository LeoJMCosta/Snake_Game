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
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



















screen.exitonclick()

#The OOP approach

# class Square:
#     def __init__(self, x, y):
#         self.t = Turtle()
#         self.t.shape('square')
#         self.t.color('white')
#         self.t.penup()
#         self.t.goto(x, y)

# def create_squares():
#     coordinates = [0, -20, -40]
#     squares = []
#     for coord in coordinates:
#         square = Square(coord, 0)
#         squares.append(square)

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')

# create_squares()
