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
    def validate_fields(self, data):
        mandatory_fields = ["name", "description", "unit_label", "unit_quantity", "unit_duration", "reminder_delay"]
        data_fields = data.keys()

        missing_fields = []

        for mandatory_field in mandatory_fields:
            if mandatory_field not in data_fields:
                missing_fields.append(mandatory_field)

        return missing_fields

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)