import random
coin = input("what is your choice: ")

flip = random.randint(0,1)
if flip == 1:
    flip = "heads"
else: 
    flip = "tails"

if coin == flip:
    print("nice choice ")
    print(f"the coin is {flip} indeed")
else:
    print(f"too bad it's {flip}")
