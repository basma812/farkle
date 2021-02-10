def keepDice(dice_list):
    chosen_dice = []
    keep_input = input(
        "Which dice do you want to keep (comma separated index: e.g. 1,1,5)? "
    )
    split_input = keep_input.split(",")

    # if the user types nothing, there is farkle:
    if keep_input == "":  # or check_farkle(dice_list):
        return dice_list, -1

    split_input_int = [int(item) for item in split_input]
    for die in split_input_int:
        chosen_dice.append(dice_list[die - 1])

    print("you want to keep:  ", chosen_dice)
    points = die * 100
    # check if you CAN save dis dice
    # if check_everything(current_dice):
    #       return chosen_dice, points?
    # else:
    #   print("wrong choice")
    return chosen_dice, points
