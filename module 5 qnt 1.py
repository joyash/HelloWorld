import random
usr = input("how many dice to roll")

roll = 0
for x in (usr):
    dice_result = random.randint(1,6)
    print(f"the dicerolled: {dice_result}")
