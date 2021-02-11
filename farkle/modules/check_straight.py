# checks if its a straight from 1-6
def check_straight(dice_list_r):
    dice_list = sorted(dice_list_r)
    if len(dice_list) != 6:
        return 0
    if dice_list[0] != dice_list[1]:
        if dice_list[1] != dice_list[2]:
            if dice_list[2] != dice_list[3]:
                if dice_list[3] != dice_list[4]:
                    if dice_list[4] != dice_list[5]:
                        return 1500

    return 0
