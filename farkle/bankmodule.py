def create_bank():
    bank = {}
    players = int(input("How many players are playing?[2-6]: "))
    for player in range(players):
        name = input(f"Enter name of player {player+1}: ")
        bank[name] = 0
    return bank
