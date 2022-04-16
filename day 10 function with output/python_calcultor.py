import os
from art import logo

def add(num1 ,num2):
    return num1 + num2

def subtract(num1 ,num2):
    return num1 - num2

def multiply(num1 ,num2):
    return num1 * num2

def division(num1 ,num2):
    return num1 / num2

def function_recurion():
    print(logo)
    num1 = int(input(("what is the first number :")))
    continue_calculation = True
    while continue_calculation:
        operators ={
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : division
            }
        for symbol in operators:
            print(symbol)

        calculate_operator = operators[input("Pick an operation from the above line:  ").title()]
        num2 = int(input(("what is the another number :")))
        answer = calculate_operator(num1,num2)
        print(answer)

        if input("select 'Y' to continue operation with same calculated no or 'N' to start new calculation : ").lower() == 'y':
            num1 = answer
        else:
            continue_calculation = False
            os.system('clear')
            function_recurion()


function_recurion()