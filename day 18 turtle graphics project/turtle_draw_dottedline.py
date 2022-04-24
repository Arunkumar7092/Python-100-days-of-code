from turtle import Turtle,Screen



krish = Turtle()
arun = Screen()
arun.bgcolor("medium turquoise")
krish.shape("turtle")

krish.pencolor("black")
krish.fillcolor("tomato")

for i in range(0, 15):
    krish.forward(10)
    krish.penup()
    krish.forward(10)
    krish.pendown()
    
arun.exitonclick()