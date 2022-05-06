from turtle import color
from numpy import multiply


def fun(**kwargs):
    for key ,value in kwargs.items():
        print(key ,":", value)


fun(name = "arun",age = 23, position = "python developer")


def calculate(a,**kwargs):
    a += kwargs["add"]
    a *= kwargs["multiply"]
    return a

    
print(calculate(8, add = 78, multiply = 56 ))


class Car():

    def __init__(self,**kwargs):
        self.model = kwargs["model"]
        self.color = kwargs.get("color")
    

car = Car(model = "Lamborgni", color = "silver")
print(car.model)
print(car.color)