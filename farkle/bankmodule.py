# creates dictionary with players names and starting values 0
import texttable as tt

table = tt.Texttable()


def create_bank():
    bank = {}
    players = int(input("How many players are playing?[2-6]: "))
    for player in range(players):
        name = input(f"Enter name of player {player+1}: ")
        bank[name] = 9000
    table.header(bank.keys())
    table.add_row(bank.values())
    return bank


# prints all players with their values in a table
def print_bank(bank):
    table.reset()
    table.header(bank.keys())
    table.add_row(bank.values())
    # table.row_width([5])
    s = table.draw()

    print(s)


# checks if any player have over 10000 points,
def check_if_over_limit(player, value):
    if value >= 10000:
        print(f"{player} has reached 10000 points! Last round begins!")
        return True
    else:
        return False


# checks and prints final Winner
def print_winner(bank):
    w = max(bank, key=bank.get)
    print("And the winner iiiiiisss....!!!!")
    print(w + " !!!  Congratz")
