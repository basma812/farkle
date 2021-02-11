from check_fourkind import check_fourkind
from check_fivekind import check_fivekind
from check_one_and_fives import check_one_and_fives
from check_sixkind import check_sixkind
from check_straight import check_straight
from check_three_pairs import check_three_pairs
from check_fourpluspair import check_fourpluspair
from ThreeOfkindcheck import trissCheck as check_triss


def check_everything(dice_list):
    sum = 0
    if check_sixkind(dice_list) > 0:
        return check_sixkind(dice_list)
    if check_straight(dice_list) > 0:
        return check_straight(dice_list)
    if check_fourpluspair(dice_list) > 0:
        return check_fourpluspair(dice_list)
    if check_three_pairs(dice_list) > 0:
        return check_three_pairs(dice_list)

    if check_fivekind(dice_list) > 0:
        sum += check_fivekind(dice_list)
        sum += check_one_and_fives(dice_list)
        return sum

    if check_fourkind(dice_list) > 0:
        sum += check_fourkind(dice_list)
        sum += check_one_and_fives(dice_list)
        return sum

    if check_triss(dice_list) > 0:
        sum += check_triss(dice_list)
        sum += check_one_and_fives(dice_list)
        return sum

    sum += check_one_and_fives(dice_list)

    return sum
