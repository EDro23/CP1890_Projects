from dataclasses import dataclass


@dataclass
class BaseballPlayer:
    first_name: str = ''
    last_name: str = ''
    position: str = ''
    at_bats: int = 0
    hits: int = 0

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def batting_avg(self) -> float:
        try:
            avg = self.hits / self.at_bats
            return avg
        except ZeroDivisionError:
            return 0.0
@dataclass
class Lineup:
    __player_list: list
    @property
    def count(self):
        return len(self.__player_list)

    def addPlayer(self, player: BaseballPlayer):
        self.__player_list.append(player)

    def removePlayer(self, number):
        self.__player_list.pop(number-1)

    def movePlayer(self, number):
        self.__player_list

    def __iter__(self):
        for player in self.__player_list:
            yield player

def main():
    lineup = Lineup([])
    lineup.addPlayer(BaseballPlayer("Ethan", "Drover", "S", 100, 100))
    lineup.addPlayer(BaseballPlayer("Buster", "Posey", "C", 4575, 1380))

    for player in lineup:
        print(f"Player: {player.fullname}")
        print(f"Batting Avg: {player.batting_avg}")
        print()

    print("Done")

if __name__ == "__main__":
    main()