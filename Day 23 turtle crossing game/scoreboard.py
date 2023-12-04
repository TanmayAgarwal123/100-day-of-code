FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", font=("Courier", 24, "normal"))
    
    def score(self):
        self.score += 1
        self.update_scoreboard()
    
    def increase_level(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
    