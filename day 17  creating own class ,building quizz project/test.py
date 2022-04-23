from class_test import Test


emp1 = Test(1034, "arun", 24)
print(emp1.id)
print(emp1.name)
print(emp1.age)

emp2 = Test(1044, "Krish", 23)
print(emp2.id)
print(emp2.name)
print(emp2.age)

emp1.increase_age(emp2)
print(emp1.age)
print(emp2.age)