import bankmodule as b


def play(bank):
    play = True
    winning_players = []
    while play:
        for player in bank.items():
            if winning_players:
                print(f"{winning_players[0]} is winning")
                # one last round has been played (player is same as
                # first in list)
                if winning_players[0] == player:
                    play = False
                    break
            points = int(input(f"how many points did {player} gain: "))
            bank[player] += points
            # every round - check winner
            if bank[player] >= 10000:
                winning_players.append(player)
                print(f"{player} has reached 10000 points! Last round begins!")

    b.print_bank(bank)
