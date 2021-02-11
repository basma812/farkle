import random
from .dicegraphic import graphic

# list of saved dices from previous throw


def diceroll(savedlist):
    d = 6 - len(savedlist)
    diceroll = []
    print("You are throwing {0} dices".format(d))
    for i in range(d):
        diceroll.append(random.randint(1, 6))
    graphic(diceroll)
    return diceroll
