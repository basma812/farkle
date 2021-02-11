# checks four of a kind plus a pair
def check_fourpluspair(dice_list):
    for i in dice_list:
        # times is how many times the element occurs in the list
        times = dice_list.count(i)
        if times == 4:
            k = i
            for j in dice_list:
                if k != j:
                    times = dice_list.count(j)
                    if times == 2:
                        return 1500
    return 0
