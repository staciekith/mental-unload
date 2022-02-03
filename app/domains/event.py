import dataclasses
import datetime

@dataclasses.dataclass
class Event:
    id: int
    title: str
    description: str
    due_date: datetime
    reminder_date: datetime
    status: str

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)