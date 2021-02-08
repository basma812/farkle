import random
def dicesroll():
    numbers = [1, 2 ,3 ,4 ,5 ,6]
    dice_list = random.choices(numbers, k = 5)
    return dice_list
