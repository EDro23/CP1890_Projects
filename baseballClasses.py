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


def test_func():
    player1 = BaseballPlayer('Ethan', 'Drover', 'S', 10, 10)
    print(f"Player: {player1.fullname}")
    print(f"Batting Avg: {player1.batting_avg}")
    print('Test complete')


if __name__ == '__main__':
    test_func()
