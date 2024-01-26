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


class Game:
    __turn: int = 1
    __score: int = 0
    __scorethisturn = 0
    __isTurnOver: bool = False
    __isGameOver: bool = False
    __die: Die = Die()

    def play(self):
        while not self.__isGameOver:
            self.takeTurn()

    def takeTurn(self):
        print('TURN', self.__turn)
        self.__scorethisturn = 0
        self.__isTurnOver = False
        while not self.__isTurnOver:
            choice = input('Roll or Hold? (r/h): ')
            if choice.lower() == 'r':
                self.roll_die()
            if choice.lower() == 'h':
                self.hold_turn()
            else:
                print('Invalid input. Check the options and try again.')

    def roll_die(self):
        self.__die.roll()
        print("Die: ", self.__die.get_value)
        if self.__die.get_value == 1:
            self.__scorethisturn = 0
            self.__turn += 1
            self.__isturnover = True
            print("This turn is over. You get no score :(\n")
        else:
            self.__scorethisturn += self.__die.get_value

    def hold_turn(self):
        self.__score += self.__scorethisturn
        self.__isTurnOver = True
        print('Score for turn: ', self.__score)
        print('Total score: ', self.__scorethisturn, '\n')
        if self.__score >= 20:
            print("Game over!")
            print("You finished in ", self.__turn, "turns!")
        else:
            self.__turn += 1
