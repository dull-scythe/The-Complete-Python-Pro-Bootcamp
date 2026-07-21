
'''
Day 4 - Exercise 2: Create an app that picks a random name from a list of friends using lists and randomisation
'''

import random

friends = ["John", "Susan", "Ethan", "Eden", "Dave", "Jonas"]
print(len(friends))

#len(friends)-1 ensures that the index is within range when randomly picking an int. Otherwise causes an error.
random_name = random.randint(0, len(friends)-1)

print(friends[random_name])



