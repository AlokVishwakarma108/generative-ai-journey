'''
Objective: Import random. Generate 5 random number between 1 to 100
Dev: Alok Vishwakarma
Date: Oct 13, 2026
'''

import random

def get_rand(itration):
  for i in range(itration):
    print(random.randint(1,100))

get_rand(5)