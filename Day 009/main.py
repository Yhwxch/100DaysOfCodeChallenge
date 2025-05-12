from art import logo
import os

print(logo)

bids = {}

while True:
    name = input('what is your name: ')
    bid = int(input('what is your bid: '))

    bids[name] = bid

    choice = input('are there any remaining bidders ?, yes/no: ')
    if choice == 'no':
        break

    os.system('cls' if os.name == 'nt' else 'clear')

highest_bidder = max(bids, key=bids.get)
print(f'the winner is {highest_bidder} with a bid of ${bids[highest_bidder]}')

