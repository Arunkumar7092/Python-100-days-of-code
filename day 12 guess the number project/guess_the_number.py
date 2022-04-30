import random
import art
# from art import logo,win_logo
import os


def choose_attempt(difficulty):
    if difficulty == 'hard':
        return 5
    else:
        return 10

def answer_check(choosen_number, guess):
    if guess > choosen_number:
        return "Too High"
    if guess < choosen_number:
        return "Too Low"
    else:
        global answer_found
        answer_found = True
        return f"You got it! The answer was {choosen_number}."

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("Guess The number between 1 and 100.")
    choosen_number = random.randint(1,100)
    # print(f"Pssst, the correct answer is {choosen_number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempt = choose_attempt(difficulty)
    global answer_found
    answer_found = False
    

    while answer_found == False:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        print(answer_check(choosen_number, guess))
        if answer_found == False:
            attempt = attempt - 1


        if attempt >= 1 and answer_found == False :
            print("Guess again.")
        elif attempt < 1:
            answer_found = True
            print("You've run out of guesses, you lose.")
            print(art.over)
        else:
            print(art.win_logo)


while input("Do you wish to play the game 'yes or 'no' :").lower() == "yes":
    os.system('clear')
    play_game()
    answer_found = False