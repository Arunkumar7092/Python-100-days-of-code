import random

word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print('''
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       

''')



chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []

for each in chosen_word:
    display += "_"
print(f"{' '.join(display)}")

end_game = False
while not end_game:
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"you already chosen {guess} ,please choose different letter")

    for position in range(word_length):
        letters = chosen_word[position]
        if guess == letters:
            display[position] = letters
    print(f"{' '.join(display)}")

    if guess not in display:
        print(stages[lives])
        lives = lives - 1

    if lives < 0:
        end_game = True
        print("you have no lives left to continue")
        print("You can't save the person from Hanging !GAME OVER")


    if "_" not in display:
        end_game = True
        print(f"You Found the word with {lives} lives left")
        print("YOU WON")
