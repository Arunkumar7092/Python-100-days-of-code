import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you wish to have in your password?:")) 
nr_symbols = int(input(f"How many symbols would you wish to have in your password?:"))
nr_numbers = int(input(f"How many numbers would you wish to have in your password?:"))

password = []
for char in range(1, nr_letters+1):
    password.append(random.choice(letters))

for symbol in range(1, nr_symbols+1):
    password.append(random.choice(symbols))

for num in range(1, nr_numbers+1):
    password.append(random.choice(numbers))


random.shuffle(password)

shuffled_password = ""

for each in password:
    shuffled_password += each
print(f"your strong password is generated which cannot be hacked: {shuffled_password}")



