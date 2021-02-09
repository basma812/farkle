def create_bank():
    bank = {}
    players = int(input("How many players are playing?[2-6]: "))
    for player in range(players):
        name = input(f"Enter name of player {player+1}: ")
        bank[name] = 0
    return bank


def print_bank(bank):
    print("|", end="")
    for player in bank.keys():
        print(f" {player}\t|", end="")
    print()
    for player in bank.keys():
        print("----------", end="")
    print()
    print("|", end="")
    for points in bank.values():
        print(f" {points}\t|", end="")
    print()
    print("|", end="")
    for points in bank.values():
        print("    \t|", end="")
