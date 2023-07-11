def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Turning Reeborg to face east (90 degrees)
turn_right()

# Creating a while loop to face Reeborg towards north.
while is_facing_north() == False:
    turn_left()

# Moving Reeborg to a position until it hits a block so at least 1 direction is blocked, to prevent it from infinitely turning right.
while front_is_clear() == True:
    move()

# Creating a while loop to continue moving until Reeborg reaches the destination in the priority order below:
# Move right, if not possible, move forward (north), if not, turn left and repeat.
while at_goal() != True:
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
