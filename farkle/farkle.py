import bankmodule as b
import playmodule as p


def main():
    # inner funtions
    bank = b.create_bank()
    b.print_bank(bank)
    p.play(bank)
    b.print_winner(bank)


if __name__ == "__main__":
    play = True
    while play:
        game = main()
        # game.Start()
        again = input("Would you like to play again? ")
        while True:
            if again.upper() in ["Y", "YE", "YES"]:
                # maybe this will work for replay
                if __name__ == "__main__":
                    main()
                break
            elif again.upper() in ["N", "NO"]:
                # trying to make it quit the game
                # or have to make a funtion for the game to quit
                play = False
                break
            else:
                print("Please enter yes or no")
