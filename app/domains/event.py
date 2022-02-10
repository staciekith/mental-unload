import dataclasses
import datetime

@dataclasses.dataclass
class Event:
    id: int
    title: str
    quantity: int
    done_at: datetime
    due_at: datetime
    remind_at: datetime
    status: str
    type_id: int

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)