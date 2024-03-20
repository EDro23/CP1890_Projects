from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    name: str
    location: str
    start_date: datetime
    end_date: datetime

    @property
    def duration(self):
        duration = (self.end_date - self.start_date)
        return duration(datetime.days)

@dataclass
class Conference(Event):
    attendees: List[str]

    @property
    def duration(self):
