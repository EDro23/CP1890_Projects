from dataclasses import dataclass

@dataclass
class StoreProducts:
    name: str = ''
    price: float = 0
    quantity: int = 0
    color: str = ''

    def __iter__(self):
        # Making the instance iterable by returning an iterator
        return iter([self.name, self.quantity, self.price, self.color])

    @property
    def total_price(self):
        return self.price * self.quantity
