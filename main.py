from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

starting_positions = [(0,0), (-20,0), (-40,0)]

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(position)



screen.exitonclick()


# The OOP approach

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
