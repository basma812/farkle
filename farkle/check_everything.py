import check_fourkind
import check_fivekind
import check_sixkind
import check_straight
import check_three_pairs


def check_everything(dice_list):
    sum = 0
    sum += check_sixkind(dice_list)
    sum += check_straight(dice_list)
    sum += check_three_pairs(dice_list)
    sum += check_fivekind(dice_list)
    sum += check_fourkind(dice_list)
    # sum += check_house(dice_list)
    # sum += check_triss(dice_list)
    # if len(dice_list < 6):
    # sum += check_one_and_fives(dice_list)
    return sum
