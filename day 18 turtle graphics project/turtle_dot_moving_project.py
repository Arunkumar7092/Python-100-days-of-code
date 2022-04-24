import turtle as t
import random
t.colormode(255)
obj = t.Turtle()
screen = t.Screen()
obj.penup()
obj.hideturtle()
obj.speed("fastest")
color = [(246, 242, 244), (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
obj.setheading(220)
obj.forward(400)
obj.setheading(0)
number_of_dots = 100
for i in range(1, number_of_dots+1):
    obj.dot(20, random.choice(color))
    obj.forward(50)
    if i % 10 == 0:
        obj.setheading(90)
        obj.forward(50)
        obj.setheading(180)
        obj.forward(500)
        obj.setheading(0)






screen.exitonclick()

# the below commented code takes colour from saved image
# import colorgram
# colours = colorgram.extract('image.jpg', 30)
# print(colours)
# rgb_colours = []
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)