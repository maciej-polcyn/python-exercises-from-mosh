import random


class Dice:
    def roll(self):
        outcome = (random.randint(1,6), random.randint(1,6))
        return outcome


dice = Dice()
print(dice.roll())

