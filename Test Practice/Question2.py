import random
from dataclasses import dataclass

@dataclass
class List:
    numbers: list[int]

@dataclass
class RandomIntList(List):
    numbers = [random.randint(0, 100)]

    @property
    def count(self):
        return len(self.numbers)

    @property
    def total(self):
        return sum(self.numbers)

    @property
    def average(self):
        return sum(self.numbers) / len(self.numbers)

    @classmethod
    def from_random(cls, n):
        return cls([random.randint(0, 100) for _ in range(n)])

    def __str__(self):
        return ', '.join(map(str, self.numbers))


def main():
    print("Random Integer List")
    print()
    while True:
        try:
            number = int(input("How many random integers should the list contain?: "))
            if number > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    int_list = RandomIntList.from_random(number)
    print("Generated Random Integer List:", int_list)
    print("Count:", int_list.count)
    print("Total:", int_list.total)
    #print("Average:", int_list.average)
    print(f"Average: {int_list.average:.3f}")

if __name__ == "__main__":
    main()


