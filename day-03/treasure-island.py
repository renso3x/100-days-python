print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

direction = input("left or right? ").lower()

if direction == 'left':
    swim_or_wait = input("swim or wait? ").lower()
    if swim_or_wait == 'wait':
        which_door = input("Which door: red, blue, yellow? ").lower()
        if which_door == 'yellow':
            print("You Won!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over.")
