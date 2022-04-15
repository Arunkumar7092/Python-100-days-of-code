from art import logo
import os
print(logo)
continue_bidding = True
bid = {}

def find_highest_bit(bidding_rec):
    highest = 0
    high_bidder = ""
    for bidding in bidding_rec:
        amount = bidding_rec[bidding]
        if amount > highest:
            highest = amount
            high_bidder = bidding
    print(f"The Winner is {high_bidder} with a bid amount of {highest}")

while continue_bidding:
    name = input("Enter Your Name :")
    print("(note:The bidder who bid for Higher amount will win these Secret Auction)")
    price = int(input("Enter your Bid Amount :"))

    
    bid[name] = price
    should_continue = input("Are there is any other bidder ? Type 'Yes' or 'No':\n").lower()
    if should_continue == "yes":
        os.system('clear')
    else:
        continue_bidding = False
        os.system('clear')
        find_highest_bit(bid)


    