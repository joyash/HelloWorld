import random
def dice_rolls(num1, num2):
    dice1 = 0
    dice2 = 0
    rolls = 0
while dice1 != num1 and dice2 != num2:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls += 1
    print(f"Rolls dice : {rolls} times")


num1 = int(input("Enter a first dice wish."))
num2 = int(input("Enter a second dice wish"))
dice_rolls(num1, num2)

