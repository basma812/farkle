def keepDice(dice_List):
    current_Dice = []
    print("Your current dices are:", dice_List)
    keep_input = input(
        "Which dice do you want to keep (comma separated: e.g. 1,1,5)? "
    )
    split_input = keep_input.split(",")
    # if the user types nothing, keep all:
    if keep_input == "":
        return dice_List
    split_input_int = [int(item) for item in split_input]
    for die in split_input_int:
        current_Dice.append(die)

    print("Your currently chosen dice to keep are: ", current_Dice)
