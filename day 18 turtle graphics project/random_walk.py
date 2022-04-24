from turtle import Turtle, Screen
import turtle as t
import random

k = Turtle()
k.pensize(15)
k.speed("fastest")
t.colormode(255)



colours = ["light salmon", "red", "green yellow", "gold", "medium purple", "light slate blue", "navy", "gray", "cadet blue", "royal blue"]
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_color = (r, g, b)
    return rgb_color


for i in range(1000):
    k.color(random_color())
    k.forward(30)
    k.setheading(random.choice(direction))
