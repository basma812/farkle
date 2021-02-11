def check_fivekind(dice_list):
    for i in dice_list:
        times = dice_list.count(i)
        if times == 5:
            return 2000
    return 0
