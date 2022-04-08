import random

names = input("Enter all the name that need to selected randomly to pay bill by placng comma after each names\n")

name_list = names.split(',')

x = len(name_list)
random_name =random.randint(0,x-1)

print(name_list[random_name])