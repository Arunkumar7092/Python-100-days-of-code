from art import logo,vs
from game_data import data
import random
import os


def statement_print(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"Compare A: {account_name}, a {account_description}, from {account_country}."

def answer_check(guess, a_follower_count, b_follower_count):
    if  a_follower_count > b_follower_count:
        if guess == "a":
            return True
    elif b_follower_count > a_follower_count:
        if guess == "b":
            return True
    else:
        return False


answer_b = random.choice(data)

game_continue = True
score = 0

while game_continue == True:
    answer_a = answer_b
    answer_b = random.choice(data)
    if answer_a == answer_b:
        answer_b = random.choice(data)
    print(logo)
    print(statement_print(answer_a))
    print(vs)
    print(statement_print(answer_b))

    a_follower_count = answer_a["follower_count"]
    b_follower_count = answer_b["follower_count"]
    print(a_follower_count)
    print(b_follower_count)
    guess = input("Who has more follower 'A' or 'B'? :").lower()



    is_correct = answer_check(guess, a_follower_count, b_follower_count)
    os.system('clear')

    if is_correct == True:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")


