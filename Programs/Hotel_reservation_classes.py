from datetime import datetime
from dataclasses import dataclass

@dataclass
class HotelReservation:
    def __init__(self, nightly_rate, hotel_name, regular_rate):
        self.nightly_rate = nightly_rate
        self.hotel_name = hotel_name
        self.regular_rate = regular_rate

    def __str__(self):
        return f'Hotel: {self.hotel_name}'

    def ArrivalDate(self):
        return datetime().strftime('%B %d, %Y')


class HotelReservations:
    nightly_rate: float
    hotel_name: str
    regular_rate: float