# checkar om det är trepar, returnerar True eller False
def check_three_pairs(dice_list_r):
    dice_list = sorted(dice_list_r)
    if len(dice_list) != 6:
        return False
    elif dice_list[0] == dice_list[1]:
        if dice_list[2] == dice_list[3]:
            if dice_list[4] == dice_list[5]:
                if dice_list[0] != dice_list[2]:
                    if dice_list[2] != dice_list[4]:
                        return 1500
    return 0
