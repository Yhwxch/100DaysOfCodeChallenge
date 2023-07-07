first_input = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if first_input == "left":
    second_input = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    if second_input == "wait":
        third_input = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower()
        if third_input == "red":
            print("You enter a room full of fire. It's too hot to handle. Game Over!")
        elif third_input == "blue":
            fourth_input = input("You enter a room with a treasure chest. It is locked! Type 'break' to break the lock or 'leave' to go back: ").lower()
            if fourth_input == "break":
                print("You successfully broke the lock and found the treasure! You win!")
            elif fourth_input == "leave":
                print("You left the room and missed the opportunity. Game Over!")
            else:
                print("You hesitate and miss your chance. Game Over!")
        elif third_input == "yellow":
            print("You enter a room full of beasts. They overpower you. Game Over!")
        else:
            print("You choose a door that does not exist. Game Over!")
    else:
        print("You dive into the lake but encounter dangerous currents. Game Over!")
else:
    print("You encounter a dead end. Game Over!")
