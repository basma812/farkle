def keepDice(dice_list):
    chosen_dice = []
    print("Your current dices are:", dice_list)
    keep_input = input(
        "Which dice do you want to keep (comma separated: e.g. 1,1,5)? "
    )
    split_input = keep_input.split(",")
    # if the user types nothing, keep all:
    if keep_input == "":
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
