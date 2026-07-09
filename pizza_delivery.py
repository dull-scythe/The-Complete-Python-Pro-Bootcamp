print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

#todo: work out how much they need to pay based on their size choice.
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L': 
    bill += 25
else:
    print("You typed the wrong inputs.")


#todo: workout how much to add their bill based on their pepperoni choice.

#first solution: using logical operators
# if pepperoni == 'Y' and size == 'S':
#     add_pepperoni = bill + 2
# if pepperoni == 'Y' and (size == 'M' or size == 'L'):
#     add_pepperoni = bill + 3
# else:
#     add_pepperoni = bill + 0

#another solution: nested if-else statement
if pepperoni == 'Y':
    if size == 'S':
        bill +=2
    else:
        bill += 3


#todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == 'Y':
    bill += 1
else: 
    bill += 0

# final_bill = bill + add_pepperoni + add_extra_cheese

print(f"Your final bill is: ${bill}")