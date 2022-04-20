# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

print("Welcome to the Love Calculator!")
print("These calculator will show your pairing % mark From 1 to 100")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_name = name1 + name2
lower_name =combined_name.lower()

T = lower_name.count("t")
R = lower_name.count("r")
U = lower_name.count("u")
E = lower_name.count("e")

true = T + R + U + E

L = lower_name.count("l")
O = lower_name.count("o")
V = lower_name.count("v")
E = lower_name.count("e")

love = L + O + V + E

result = str(true)+str(love)

final_result = int(result)

if final_result < 10 or final_result > 90:
    print(f"Your score is {final_result}, you go together like coke and mentos.")
elif final_result > 40 and final_result < 50:
    print(f"Your score is {final_result}, you are alright together.")
else:
    print(f"Your score is {final_result}, Wow you got awesome Score")
