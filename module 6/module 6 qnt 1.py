import random

def dice_roll():
    dice1 = 0
    rolls = 0
    while dice1 != 6:
         dice1 = random.randint(1, 6)
         print(f"roll {rolls + 1} : {dice1}")
         rolls += 1
         """if(dice1 == 6):
               break"""
    print(f"value: {dice1} and rolls: {rolls}")

dice_roll()