print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
      ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = str(input("Would you like to go left or right? "))
if direction == 'left' or 'Left':
    print("You decided to go left.")
    movement = str(input("Would you like to swim or wait? "))
    if movement == 'wait' or 'Wait':
        print("You decided to wait. Being still has its advantages...")
        door = str(input("Please pick a door to go through: Red, Blue, or Yellow? "))
        if door == 'yellow' or 'Yellow':
            print("Congratulations! You found the hidden treasure!!!")
            print("Excelsior!")
        elif door == 'red' or 'Red':
            print("This ain't the matrix...")
            print("AHHHH! You were burned by fire!")
            print("Game over.")
        elif door == 'blue' or 'Blue':
            print("This ain't the matrix...")
            print("AHHHHHH! You were eaten by beasts!")
            print("Game over.")
        else:
            print("You input the wrong answer. Game over.")
    elif movement == 'swim' or 'Swim':
        print("Uh oh... swimming has consequencs...")
        print("CHOMP! You were attacked by a giant trout.")
        print("Game over.")
    else:
        print("CHOMP! You were attacked by a giant trout.")
        print("Game over.") 
elif direction == 'right' or 'Right':
    print("Did you make the RIGHT decision?...")
    print("Oh no! You fell into a hole!")
    print("Game over.")
else:
    print("Oh no! You fell into a hole!")
    print("Game over.")


