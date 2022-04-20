# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
bill = 0

if size == "s" or size == "S" :
    bill = 15
    if add_pepperoni == "y" and extra_cheese == "y":
        bill+=2+1
    elif extra_cheese == "y" and add_pepperoni == "n":
        bill+=1
    elif extra_cheese == "n" and add_pepperoni == "y":
        bill+=2

elif size == "m" or size == "M":
    bill = 20
    if add_pepperoni == "y" and extra_cheese == "y":
        bill+=3+1
    elif extra_cheese == "y" and add_pepperoni == "n":
        bill+=1
    elif extra_cheese == "n" and add_pepperoni == "y":
        bill+=3

elif size == "l" or size == "L":
    bill = 25
    if add_pepperoni == "y" and extra_cheese == "y":
        bill+=3+1
    elif extra_cheese == "y" and add_pepperoni == "n":
        bill+=1
    elif extra_cheese == "n" and add_pepperoni == "y":
        bill+=3

print(f"Your final bill is: ${bill}.")
