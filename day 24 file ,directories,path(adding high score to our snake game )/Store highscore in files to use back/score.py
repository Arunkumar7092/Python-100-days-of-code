from turtle import Turtle
# import os

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/home/developer/Desktop/arun-100/python-100-days/day 24 file ,directories,path(adding high score to our snake game )/Store highscore in files to use back/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score :{self.score} / High score:{self.high_score}",align ="center", font = ("Arial",24,"normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/home/developer/Desktop/arun-100/python-100-days/day 24 file ,directories,path(adding high score to our snake game )/Store highscore in files to use back/data.txt",mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align ="center", font = ("Arial",24,"normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
