# i was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.


# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

age = input("What is your current age?")


rem_age = 90 - int(age)
rem_days = rem_age * 365
rem_week = rem_age * 52
rem_month = rem_age * 12
print(f"You have {rem_days} days, {rem_week} weeks, and {rem_month} months left.") 
