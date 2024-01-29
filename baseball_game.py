from datetime import datetime
from baseballClasses import BaseballPlayer

def divider():
    print(50 * "=")

def menutop(gamedayinput=None):
    print("\t\t\t\tBaseball Team Manager")
    print()
    print("CURRENT DATE:", datetime.now())  # Corrected line
    print(f"GAME DATE: {user_input}")
    print("Days until next game:")
    print()

def menu_options():
    print("MENU OPTIONS")
    print(" 1 - Display lineup\n",
          "2 - Add player\n",
          "3 - Remove player\n",
          "4 - Move player\n",
          "5 - Edit player position\n",
          "6 - Edit player stats\n",
          "7 - Exit program\n")

def positions():
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

def main(self=None):
    game_day_input()
    divider()
    menutop()
    menu_options()
    positions()
    divider()
    option = input("Menu option: ")
    if option == "1":
        game = BaseballPlayer
        game.display_lineup(self)

if __name__ == "__main__":
    main()

