from turtle import Turtle,Screen
import random

colours = ["light salmon", "red", "green yellow", "gold", "medium purple", "light slate blue", "navy", "gray", "cadet blue", "royal blue"]
krish = Turtle()
arun = Screen()
arun.bgcolor("white")
krish.shape("turtle")

krish.pencolor("black")
krish.fillcolor("tomato")

def draw_shapes_down(sides):
    angle = 360/sides
    for _ in range(sides):
        krish.forward(100)
        krish.right(angle)

def draw_shapes_front(sides):
    angle = 360/sides
    for _ in range(sides):
        krish.forward(100)
        krish.left(angle)

for i in range(3, 10):
    krish.pencolor(random.choice(colours))
    draw_shapes_down(i)
for i in range(3, 10):
    krish.pencolor(random.choice(colours))
    draw_shapes_front(i)

arun.exitonclick()