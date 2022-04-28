from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.refresh_food()
    

    def refresh_food(self):
        xcord = random.randint(-270,270)
        ycord = random.randint(-270,270)
        self.goto(xcord,ycord)


