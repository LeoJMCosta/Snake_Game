from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  
        self.goto(0, 265)
        self.score = 0
        self.write(f'Score = {self.score}', align='center', font=('Arial', 20, 'normal'))
    
    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}', align='center', font=('Arial', 20, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.update_score()

        
