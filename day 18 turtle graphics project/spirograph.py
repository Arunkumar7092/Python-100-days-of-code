from turtle import Turtle, Screen
import turtle as t
import random

k = Turtle()
s = Screen()
k.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_color = (r, g, b)
    return rgb_color

def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        k.color(random_color())
        k.circle(100)
        k.setheading(k.heading() + gap_size)


draw_spirograph(3)
s.exitonclick()