from pig_classes import Game


def pig_game():
    print("Let's Play PIG!!")
    print("Here are the rules!"
          "\n* See how many turns it takes you to get to 20."
          "\n* Turn ends when you hold or roll a 1."
          "\n* If you roll a 1, you lose all your points for that turn."
          "\n* If you hold, you save all points for that turn.\n")


def main():
    pig_game()
    choice = 'y'
    while choice.lower() == 'y':
        game = Game()
        game.play()

        choice = input("Play again? (Y/N): ")
        print()
        print("Thanks for playing")

        if __name__ == '__main__':
            main()
