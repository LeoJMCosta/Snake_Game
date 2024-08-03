from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  
        self.goto(0, 265)
        self.score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game over', align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_score()

        
