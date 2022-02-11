import dataclasses
import json

@dataclasses.dataclass
class EventType:
    id: int
    name: str
    description: str
    unit_label: str
    unit_quantity: int
    unit_duration: int
    reminder_delay: int

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)