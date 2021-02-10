import bankmodule as b
import keepDice as k
import diceroll as d
import os
import dicegraphic as dg


def cls():
    os.system("cls")


def play(bank):
    play = True
    winning_players = []
    dices = []
    newdices = []

    while play:
        # loop for every round
        for player, values in bank.items():
            round_points = 0
            # if someone has over 10000
            if winning_players:
                # check if the last round has played?
                if winning_players[0] == player:
                    play = False
                    break

            input_choice = input(f"Do {player} want to throw [y/n]: ")
            while input_choice == "y":

                newdices = d.diceroll(dices)
                newdices, points = k.keepDice(newdices)

                # farkle, didnt get combination
                if points == -1:
                    print("You got farkle, next player turn")
                    dices = []
                    break
                else:
                    dices.extend(newdices)
                    print("your dices ===")
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
            if bank[player] >= 10000:
                winning_players.append(player)
                print(f"{player} has reached 10000 points! Last round begins!")

    cls()
    b.print_bank(bank)
