import bankmodule as b
import keepDice as k
import diceroll as d
import os


def cls():
    os.system("cls")


def play(bank):
    play = True
    winning_players = []
    dices = []
    while play:
        for player, values in bank.items():
            if winning_players:
                if winning_players[0] == player:
                    play = False
                    break

            # points = int(input(f"how many points did {player} gain: "))
            input_choice = input("Do you want to HIT")
            while input_choice == "y":
                d.diceroll(dices)
                dices = k.keepDice(dices)
            # bank[player] += points
            # every round - check winner
            if bank[player] >= 10000:
                winning_players.append(player)
                print(f"{player} has reached 10000 points! Last round begins!")
    cls()
    b.print_bank(bank)
