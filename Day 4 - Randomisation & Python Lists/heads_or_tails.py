'''
Day 4 - Exercise 1: Create a Heads or Tails generator using the random module
'''

import random

coin_flip = random.randint(0,1)

if coin_flip == 0:
    print("Heads")
else:
    print("Tails")
    
