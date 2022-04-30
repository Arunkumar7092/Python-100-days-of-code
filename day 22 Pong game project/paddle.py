from turtle import Turtle

PADDLE_POSITION = [(-380, 0),(380,0)]
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len= 1 )
        self.color("white")
        self.penup()
        self.speed("fastest")

    
    def set_player1_position(self):
        self.goto(PADDLE_POSITION[0])
    
    def set_player2_position(self):
        self.goto(PADDLE_POSITION[1])

    def up(self):
        if self.ycor() < 240:
            y_pos = self.ycor() + 40
            self.goto(self.xcor(),y_pos)
    

    def down(self):
        if self.ycor() > -240:
            y_pos = self.ycor() - 40
            self.goto(self.xcor(),y_pos)
