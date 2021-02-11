import bankmodule as b
import keepDice as k
import diceroll as d
import os
import dicegraphic as dg
import check_deposit500 as cd
import time


def cls():
    os.system("cls")


def play(bank):
    play = True
    winning_player = ""
    dices = []
    newdices = []
    farklecount = {}
    for player in bank.keys():
        farklecount[player] = 0

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
                    farklecount[player] += 1
                    if farklecount[player] == 3:
                        bank[player] -= 500
                        print("Triple Farkle! you loose 500 points! ")
                    dices = []
                    break
                else:
                    farklecount[player] = 0
                    dices.extend(newdices)
                    print(" === your saved dices === ")
                    dg.graphic(dices)

                    if len(dices) == 6:
                        print("Dices reset, full hand(you got 6 dices again) ")
                        dices = []

                    round_points += points
                    print("Points this round: ", round_points)
                    input_choice = input(
                        f"Do {player} want to "
                        "throw your remaining dices?: [y/n]"
                    )
                    # stay/save to bank
                    if input_choice == "n":
                        cd.check_deposit500(player, bank, round_points)
                        dices = []
                        continue

            # every round - check winner
            if bank[player] >= 10000 and winning_player == "":
                winning_player = player
                print(f"{player} has reached 10000 points! Last round begins!")

            time.sleep(1)
            cls()
            b.print_bank(bank)
