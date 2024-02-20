from dataclasses import dataclass

@dataclass
class Product:
    name: str = ""
    price: float = 0.0
    quantity: int = 0
    discount: float = 0.0
    description: str = ""

    def getName(self) -> str:
        return self.name

    def getPrice(self) -> float:
        return self.price

    def getQuantity(self) -> int:
        return self.quantity

    def getDiscount(self) -> float:
        return self.price * self.discount / 100

    def getTotalPrice(self) -> float:
        return self.price - self.getDiscount()

    def getDescription(self) -> str:
        print("PRODUCT DATA")
        return f"Name: {self.getName()}\nPrice: {self.getPrice()}\nQuantity: {self.getQuantity()}\nDiscount: {self.getDiscount()}\nTotal: {self.getTotalPrice()}"

@dataclass
class Item(Product):
    name: str = ""

    def getName(self) -> str:
        return self.name

    def getPrice(self) -> int:
        return int(self.price)

    def getQuantity(self) -> int:
        return self.quantity

    def getDiscount(self) -> float:
        return self.price * self.discount / 100

    def getDescription(self) -> str:
        return (f"Name: {self.getName()}\n"
                f"Discount price: {self.getDiscount()}\n"
                f"Quantity: {self.getQuantity()}\n"
                f"Price: {self.getPrice()}\n"
                f"Discount: {self.getDiscount()}\n"
                f"Total: {self.getTotalPrice()}")

@dataclass
class Movies(Product):
    name: str = ""
    year: int = 0

    def getName(self) -> str:
        return self.name

    def getYear(self) -> int:
        return self.year

    def getDescription(self) -> str:
        return (f"Name: {self.getName()}\n"
                f"Discount price: {self.getDiscount()}")

item1 = Item("Stanley 13 Ounce Wood Hammer", 10, 2, 5, "Hammer")
movie1 = Movies("The Holy Grail", 20, 1, 5, "DVD", 1975)

print("PRODUCT DATA")
print(item1.getDescription())
print()
print("PRODUCT DATA")
print(movie1.getDescription())