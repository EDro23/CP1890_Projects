from dataclasses import dataclass

class Fruit:
    def __init__(self, name: str, color: str, calories: float):
        self.name = name
        self.color = color
        self.calories = calories

banana = Fruit('Banana', 'yellow',10)
banana2d = Fruit('Banana', 'yellow',10)
apple = Fruit('Apple', 'red',20)

print(banana.calories)

@dataclass
class FruitD:
    name: str
    color: str
    calories: float

bananad = FruitD('Banana', 'yellow',10)
appled = FruitD('Apple', 'red',20)

print(appled)
print(banana == bananad)
print(bananad == banana2d)
