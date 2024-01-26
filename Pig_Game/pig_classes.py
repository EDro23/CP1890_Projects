
import random
from dataclasses import dataclass
@Dataclass
class Die:
    __value: int = 1

    def roll(self):
        self.__value = random.randint(1, 6)
    @property
    def get_value(self):
        return self.__value
class game:
    def player_turn(self):
        while True:
            playerpoints = 0






