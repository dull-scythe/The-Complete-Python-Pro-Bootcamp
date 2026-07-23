import random


print("Welcome to ROCK PAPER SCISSORS!")
print("Type 0 for Rock")
print("Type 1 for Paper")
print("Type 2 for Scissors")

choice = int(input())

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

if choice == 0:
    '''
    print ascii for rock
    '''
    print(rock)

elif choice == 1:
    '''
    print ascii for paper
    '''
    print(paper)
elif choice == 2:
    '''
    print ascii for scissors
    '''
    print(scissors)
else:
    print("Wrong input. Game over!")


'''
Need to implement randomisation of computer's choice using control flow and random module
'''

computer_choice = random.randomint() 

print(computer_choice)
