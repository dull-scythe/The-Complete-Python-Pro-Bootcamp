print("Welcome to the rollercoaster!")
print("You have to be 120cm or taller to ride the rollercoaster")
height = int(input("How tall are you?"))

#My solution
# if height >= 120:
#     print("You can ride!")
# else: 
#     print("You can't ride :(")

# age = int(input("How old are you?"))
# bill = 0 

# if age < 12: 
#     bill += 5
# elif age >= 12 and age <= 18:
#     bill += 7
# elif age > 18 and age < 45:
#     bill += 12
# elif age >= 45 and age <=55:
#     bill += 0

# photos = input("Do you want photos?")

# if photos == 'Y' or photos == 'y':
#     bill += 3
# if photos == 'N' or photos == 'n':
#     bill += 0

# print(f"The total bill is: ${bill}")


#BootCamp Solution
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?" ))
    if age < 12: 
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photos = input("Do you want a photo taken? Y or N")
    if wants_photos == 'Y':
        bill += 3

    print(f"Your total bill is ${bill})")
else:
    print("Sorry, you have to grow taller before you can ride.")

