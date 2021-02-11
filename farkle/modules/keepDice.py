from .check_everything import check_everything


def keepDice(dice_list):
    chosen_dice = []
    # farkle
    if check_everything(dice_list) == 0:
        return dice_list, -1

    keep_input = input(
        "Which dice do you want to keep (comma separated index: e.g. 1,1,5)? "
    )
    split_input = keep_input.split(",")

    # if the user types nothing, there is farkle:

    split_input_int = [int(item) for item in split_input]
    for die in split_input_int:
        chosen_dice.append(dice_list[die - 1])

    print("You want to keep:  ", chosen_dice)
    points = check_everything(chosen_dice)
    if points == 0:
        print("No combination found ")
    # check if you CAN save dis dice
    # if check_everything(current_dice):
    #       return chosen_dice, points?
    # else:
    #   print("wrong choice")
    return chosen_dice, points


# import re
# def getFarkle(current_player, farkleCount, farklepattren):
# farklepattren == "[2-46]"
# 	if diceroll =! re.match(farklepattren)
# 		print ("FARKLE"),
# 		if farkleCount == 3:
# 			print(-500)
# 	else:
# 		continue
