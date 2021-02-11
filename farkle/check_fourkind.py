def check_fourkind(dice_list):
    for i in dice_list:
        times = dice_list.count(i)
        if times == 4:
            return 1000
    return 0
