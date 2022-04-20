# If the bill was $150.00, split between 5 people, with 12% tip.


# Input format

# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ = "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
tip_with_bill = bill + bill * tip_percentage
total_amount = tip_with_bill/people
print(f"Each person should pay $ = " "{:.2f}".format(total_amount))
