from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280
FACING_DIRECTION = 90


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(FACING_DIRECTION)
    
    def turtle_move(self):
        self.forward(MOVE_DISTANCE)


    def is_at_finish(self):
        if self.ycor() >  FINISH_LINE_Y:
           return True
        else:
            return False
    
    def goto_start(self):
        self.goto(STARTING_POSITION)

        
