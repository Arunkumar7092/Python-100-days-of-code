# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


h = float(height)
w = float(weight)
bmi = int(w/(h*h))
print(bmi)