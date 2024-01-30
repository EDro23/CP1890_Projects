from baseballClasses import BaseballPlayer
from datetime import datetime

POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')


def dateandtime():
    print("CURRENT DATE: ", datetime.now().strftime("%y/%m/%d"))
    gamedate = input("GAME DATE: \t")
    # days_until_game = datetime.strftime(gamedate, "%y/%m/%d").date() - datetime.now().strftime("%y/%m/%d")


def add_player(players):
    first_name = input('First name: ').title()
    last_name = input('Last name: ').title()
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)
    # full_name = f'{first_name} {last_name}'

    player = BaseballPlayer(first_name, last_name, position, at_bats, hits)
    players.append(player)
    print(f'Player {player.first_name} {player.last_name} was added.')


def get_player_position():
    while True:
        position = input('Position: ').upper()
        if position in POSITIONS:
            return position
        else:
            print('Invalid position. Please enter correctly.')
            print('Valid positions are: ' + ', '.join(POSITIONS))


def get_at_bats():
    while True:
        try:
            at_bats = int(input('At bats: '))
        except ValueError:
            print('Invalid input. Please enter correctly.')
            continue
        if at_bats < 0 or at_bats > 500:
            print('Invalid entry. Must be between 0 and 500')
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input('Hits: '))
        except ValueError:
            print('Invalid input. Please try again.')
            continue
        if hits < 0 or hits > at_bats:
            print(f'Invalid entry. Must be between 0 and {at_bats}')
        else:
            return hits


def display_lineup(players):
    if players is None:
        print('No players in lineup.')
    else:
        print(f"{'':3}{'Player':40}{'POS':6}{'AB':>4}\t{'HITS':>6}{'AVG':>8}")
        print('-' * 80)
        for i, player in enumerate(players):
            print(
                f'{i + 1:<3d}{player.first_name.ljust(1)} {player.last_name.ljust(29)} {player.position.rjust(6)}\t{str(player.at_bats).rjust(6)} {str(player.hits).rjust(6)}\t\t{player.batting_avg:.3f}')
        print()


def remove_player(players):
    try:
        if players is None:
            print("No players in lineup")
        else:
            choice = input(f'\nWho would you like to remove? (Select by first name, CASE SENSITIVE): ')
    except ValueError:
        print('Invalid, please try again.')
    try:
        for player in players:
            if choice == player.first_name:
                players.remove(player)
                print(f'{choice} has been succesfully removed!')
            else:
                print('Sorry :(\nInvalid name in list of players, please try again.')
    except ValueError:
        print('Invalid, please try again.')


def move_player(players):
    try:
        if not players:
            print("No players in lineup")
        else:
            choice = input('\nWho would you like to move? (Select by first name): ')
            player_found = False

            for player in players:
                if choice.lower() == player.first_name.lower():
                    player_found = True
                    move_player_num = int(
                        input(f"Which number would you like to move {player.first_name} to? (1-{len(players)}): "))
                    if 1 <= move_player_num <= len(players):
                        # Remove the player from the current position and insert at the new position.
                        players.remove(player)
                        players.insert(move_player_num - 1, player)
                        print("Loading...")
                        print(".\n.\n.")
                        print(f"{player.first_name} has been successfully moved!")
                        break
                    else:
                        print(f"Invalid position. Please enter a number between 1 and {len(players)}")

            if not player_found:
                print('Sorry :(\nInvalid, player not in lineup.\nPlease try again.')

    except Exception:
        print('Invalid, please try again.')


def edit_player_position(players, POSITIONS):
    while True:
        try:
            if not players:
                print('Player not in lineup.\nPlease try again.')
            else:
                choice = input("Who would you like to edit the position for? (Enter first name): ")
                # Check if the entered name is in any player's first name
                if not any(player.first_name == choice for player in players):
                    print('This player does not exist. Try again.')
                else:
                    print('Valid positions are: ' + ', '.join(POSITIONS))
                    poschoice = input(f"\nWhich position would you like to move {choice} to?: ")
                    if poschoice.upper() not in POSITIONS:
                        print('Invalid position. Please try again.')
                    else:
                        for player in players:
                            if player.first_name == choice.title():
                                player.position = poschoice.upper()
                                print(f"Position has been successfully changed for {player.first_name}.")
                        break
        except Exception:
            print('Invalid, please try again.')


def display_seperator():
    print('-' * 80)


def display_title():
    print('\t\t\t\t Baseball Team Manager')


def display_options():
    print('Menu Options')
    print(" 1 - Display lineup\n",
          "2 - Add player\n",
          "3 - Remove player\n",
          "4 - Move player\n",
          "5 - Edit player position\n",
          "6 - Edit player stats\n",
          "7 - Exit program\n")


def display_positions(POSITIONS):
    print('POSITIONS')
    print(','.join(POSITIONS))


def main():
    display_seperator()
    display_title()
    dateandtime()
    display_options()
    display_positions(POSITIONS)
    display_seperator()

    players = []

    while True:
        try:
            choice = int(input('Menu option: '))
        except ValueError:
            choice = -1

        if choice == 1:
            display_lineup(players)
        elif choice == 2:
            add_player(players)
        elif choice == 3:
            remove_player(players)
        elif choice == 4:
            move_player(players)
        elif choice == 5:
            edit_player_position(players,POSITIONS)
        elif choice == 7:
            print("Bye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
