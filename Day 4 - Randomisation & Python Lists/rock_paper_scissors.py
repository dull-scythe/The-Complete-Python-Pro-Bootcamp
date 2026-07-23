import random


print("Welcome to ROCK PAPER SCISSORS!")
print("Type 0 for Rock")
print("Type 1 for Paper")
print("Type 2 for Scissors")

user_choice = int(input())

#Need to implement randomisation of computer's choice using control flow and random module
computer_choice = random.randint(0, 2) 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# if user_choice == 0:
#     '''
#     print ascii for rock
#     '''
#     print(rock)

# elif user_choice == 1:
#     '''
#     print ascii for paper
#     '''
#     print(paper)
# elif user_choice == 2:
#     '''
#     print ascii for scissors
#     '''
#     print(scissors)
# else:
#     print("Wrong input. Game over!")

# if computer_choice == 0:
#     '''
#     print ascii for rock
#     '''
#     print(rock)

# elif computer_choice == 1:
#     '''
#     print ascii for paper
#     '''
#     print(paper)
# else:
#     '''
#     print ascii for scissors
#     '''
#     print(scissors)

'''
Implement control flow for matches by comparing user vs computer
'''

if user_choice == 0 and computer_choice == 0:
    print(rock)
    print(rock) 
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 1:
    print(rock)
    print(paper)
    print("You lost. Paper beats Rock.")
elif user_choice == 0 and computer_choice == 2:
    print(rock)
    print(scissors) 
    print("You won! Rock beats Scissors.")
elif user_choice == 1 and computer_choice == 0:
    print(paper)
    print(rock) 
    print("You won! Paper beats Rock.")
elif user_choice == 1 and computer_choice == 1:
    print(paper)
    print(paper)
    print("It's a draw!")
elif user_choice == 1 and computer_choice == 2:
    print(paper)
    print(scissors) 
    print("You lost. Scissors beats Paper.")
elif user_choice == 2 and computer_choice == 0:
    print(scissors)
    print(rock) 
    print("You lost. Rock beats Scissors.")
elif user_choice == 2 and computer_choice == 1:
    print(scissors)
    print(paper)
    print("You won! Scissors beats Paper.")
elif user_choice == 2 and computer_choice == 2: 
    print(scissors)
    print(scissors)
    print("It's a draw!")
