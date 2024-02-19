from dataclasses import dataclass

@dataclass
class Theater:
    location: str = ""
    capacity: int = 0
    ticketPrice: float = 0.0

    def getLocation(self) -> str:
        return self.location

    def getCapacity(self) -> int:
        return self.capacity

    def getDescription(self) -> str:
        return f"{self.location} with a capactiy of {self.capacity}, Ticket cost is ${self.ticketPrice}"

    def getTicketPrice(self) -> float:
        return self.ticketPrice


@dataclass
class Movie:
    name: str = ""
    year: int = 0

    def getName(self) -> str:
        return self.name

    def getYear(self) -> int:
        return self.year

    def getDescription(self) -> str:
        return f"{self.name}, Released in {self.year}"

theater1 = Theater("Scotiabank Theater", 200, 7)
movie1 = Movie("Venom", 2013)

print(theater1.getDescription())
print(movie1.getDescription())