def check_sixkind(dice_list):
    for i in dice_list:
        times = dice_list.count(i)
        if times == 6:
            if i == 1:
                return 10000
            return 3000
    return 0
