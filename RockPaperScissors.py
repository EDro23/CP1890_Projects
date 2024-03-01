from dataclasses import dataclass
import random

ROSHAMBO_COLL = ('rock', 'paper', 'scissors')

@dataclass
class Player:
    def __init__(self, name, roshambo):
        self.name = name
        self.roshambo = roshambo
        self.__wins: int = 0
        self.__losses: int = 0

    def generateRoshambo(self):
        return self.roshambo

    @classmethod
    def play(cls, player1, player2):
        if player1.roshambo == player2.roshambo:
            return None
        else:
            if (player1.roshambo == 'rock' and player2.roshambo == 'scissors') \
                or (player1.roshambo == 'paper' and player2.roshambo == 'rock') \
                    or (player1.roshambo == 'scissors' and player2.roshambo == 'paper'):
                return player1
            else:
                return player2

    @property
    def wins(self) -> int:
        return self.__wins

    @property
    def losses(self):
        return self.__losses

    def addWin(self):
        self.__wins += 1

    def addLoss(self):
        self.__losses += 1

    def __str__(self):
        return f'{self.name}: {self.roshambo}'


@dataclass
class Bart(Player):
    def __post_init__(self):
        self.name = 'Bart'
        super().__init__(self.name, random.choice(ROSHAMBO_COLL))


@dataclass
class Lisa(Player):
    def __post_init__(self):
        self.name = 'Lisa'
        super().__init__(self.name, random.choice(ROSHAMBO_COLL))

def main():
    print("Roshambo Game\n")
    name = input("What is your name?: ")
    print()

    player1 = Player(name, random.choice(ROSHAMBO_COLL))

    opponent = input("Would you like to play against Bart or Lisa? (b/l): ")
    print()

    opponent_chosen = 'n'
    while opponent_chosen == 'n':
        if opponent.lower() == 'b':
            player2 = Bart()
            opponent_chosen = 'y'
        elif opponent.lower() == 'l':
            player2 = Lisa()
            opponent_chosen = 'y'
        else:
            print("Invalid choice, choose between Bart or Lisa")

    play_again = 'y'
    while play_again.lower() == 'y':
        # Get Roshambo for player 1
        selection = input('Rock, Paper, Scissors? (r/p/s): ').lower()
        print()
        if selection == 'r':
            player1.roshambo = 'rock'
        elif selection == 'p':
            player1.roshambo = 'paper'
        elif selection == 's':
            player1.roshambo = 'scissors'
        else:
            print('Invalid choice, select again!')
            continue

        # Get Roshambo for player 2
        player2.generateRoshambo()

        # Displaying names and state
        print(player1)
        print(player2)

        # Start the game
        winner = Player.play(player1, player2)
        if winner is None:
            print('Draw!')
            print()
        else:
            print(f'{winner.name} Wins!')
            winner.addWin()
            if winner is player1:
                player2.addLoss()
            else:
                player1.addLoss()

        # Displaying totals for each player
        print(f'{player1.name}: {player1.wins} total win(s), {player1.losses}: Total loss(es)')
        print(f'{player2.name}: {player2.wins} total win(s), {player2.losses}: Total loss(es)')
        print()

        play_again = input('Play again? (y/n): ').lower()
        print()

    print("Thanks for playing Roshambo")

if __name__ == '__main__':
    main()



