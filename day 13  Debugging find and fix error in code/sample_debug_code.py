# Uncomment segement wise and Sqash the bug
# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
"""
Solution for above bug is for loop will run from 1 to 19 and the condtion statemet is used their is to print at when i is 20 .
In such a case these will never met condition.

Answer:

def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

"""

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

"""
Solution for above bug is :
if you run the above code again and again at some point you will get the error index out of range .
so every time done with code run the code as many time you can and check for the output.

the error is caused due to the list dice_imgs have index from 0 to 5 .
but the randint will generate random number till 6 and it will not use index 0 at any point .
to run the code in right way use the dice_num = randint(0, 5)
"""

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

"""
Solution for above bug is :
The above code will run fine as long as you input the number 1994.
the condition used above is will acess data greater than 1994 and lesser than 1994 .
so also to aceess the input of 1994 use condition = statement to solve the bug.
"""

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

"""
Solution for above bug is :

The imput of above code will be stored in string format but the condition used is integer.
print statement you try to print string directly without using f"{fstring}"
get input using int(input())

"""

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

"""
Solution for above bug is :

If you run the above code you will get the answer as 0 .
These is beacuse used == for variable word_per_page .

"""
# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   print(new_item)  
#   b_list.append(new_item)
#   print(b_list)
# mutate([1,2,3,5,8,13])




"""
Solution for above bug is :
The above code will work but it will print the b_list with value of a_list last value *2 .
because appending b_list out side the for loop will append last stored new_item variable value 

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

"""