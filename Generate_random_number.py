# generate random number

import random

def randomnum():
    num = random.randint(0,1000)
    return num

print("Randomly generated value = ",randomnum())