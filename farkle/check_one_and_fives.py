# vi ska checka ettor och femmor. ettor ger 100 styck och femmor 50.
# först måste vi kolla så att det inte är ettor eller femmor i triss,
# fyrtal, eller femtal
# t ex om det är ettor i triss och vi har två femmor. då ska vi inte checka
# efter ettor
# eftersom de redan är i trissen


def checkones(dice_list):
    for i in dice_list:
        if i == 1:
            times = dice_list.count(i)
            if times == 1:
                return 100
            if times == 2:
                return 200
    return 0


def checkfives(dice_list):
    for i in dice_list:
        if i == 5:
            times = dice_list.count(i)
            if times == 1:
                return 50
            if times == 2:
                return 100
    return 0


def check_one_and_fives(dice_list):
    for i in dice_list:
        times = dice_list.count(i)
        if times == 5:
            if i == 5:
                return checkones(dice_list)
            if i == 1:
                return checkfives(dice_list)
        elif times == 4:
            if i == 5:
                return checkones(dice_list)
            if i == 1:
                return checkfives(dice_list)
        elif times == 3:
            if i == 5:
                return checkones(dice_list)
            if i == 1:
                return checkfives(dice_list)
        else:
            for i in dice_list:
                if i == 1:
                    times = dice_list.count(i)
                    if times == 1:
                        return 100
                    if times == 2:
                        return 200
                if i == 5:
                    times = dice_list.count(i)
                    if times == 1:
                        return 50
                    if times == 2:
                        return 100
    return 0
