# creates dictionary with players names and starting values 0
def create_bank():
    bank = {}
    players = int(input("How many players are playing?[2-6]: "))
    for player in range(players):
        name = input(f"Enter name of player {player+1}: ")
        bank[name] = 0
    return bank


# prints all players with their values in a table
def print_bank(bank):
    print("|", end="")
    for player in bank.keys():
        print(f" {player}\t\t|", end="")
    print()
    for player in bank.keys():
        print("--------------------", end="")
    print()
    print("|", end="")
    for points in bank.values():
        print(f" {points}\t\t|", end="")
    print()
    print("|", end="")
    for points in bank.values():
        print("    \t\t|", end="")
    print()


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
