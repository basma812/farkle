import bankmodule as b
import keepDice as k
import diceroll as d
import os
import dicegraphic as dg


def cls():
    os.system("cls")


def play(bank):
    play = True
    winning_player = ""
    dices = []
    newdices = []

    while play:
        # loop for every round
        for player, _ in bank.items():
            round_points = 0
            print(f"{player.upper()}'s round!!!!!!")
            # if someone has over 10000
            if winning_player:
                # check if the last round has played?
                if winning_player == player:
                    play = False
                    break

            # "throwing dices"-loop ( a player-round )
            input_choice = input(f"Do {player} want to throw dices [y/n]: ")
            while input_choice == "y":

                newdices = d.diceroll(dices)
                # choose which dices to keep, and check points
                newdices, points = k.keepDice(newdices)

                # farkle, didnt get combination
                if points == -1:
                    print("You got farkle, next player turn")
                    dices = []
                    break
                else:
                    dices.extend(newdices)
                    print(" === your saved dices === ")
                    dg.graphic(dices)

                    if len(dices) == 6:
                        print("dices reset, full hand(you got 6 dices again")
                        dices = []

                    round_points += points
                    print("current points = ", round_points)
                    input_choice = input(
                        f"Do {player} want to "
                        "throw your remaining dices?: [y/n]"
                    )
                    # stay/save to bank
                    if input_choice == "n":
                        bank[player] += round_points
                        dices = []
                        continue

            # every round - check winner
            if bank[player] >= 10000 and winning_player == "":
                winning_player = player
                print(f"{player} has reached 10000 points! Last round begins!")

            cls()
            b.print_bank(bank)
