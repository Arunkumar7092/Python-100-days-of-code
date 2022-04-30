from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-100,260)
        self.write(self.l_score,align ="center", font = ("Arial",24,"normal"))
        self.goto(100,260)
        self.write(self.r_score,align ="center", font = ("Arial",24,"normal"))


    def player1_wins(self):
        self.goto(0,0)
        self.write("Player 1 wins with 5 points",align ="center", font = ("Arial",24,"normal"))


    def player2_wins(self):
        self.goto(0,0)
        self.write("Player 2 wins with 5 points",align ="center", font = ("Arial",24,"normal"))


    def increase_player2_score(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
    
    def increase_player1_score(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()