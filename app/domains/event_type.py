import dataclasses

@dataclasses.dataclass
class EventType:
    id: int
    name: str
    description: str
    unit_label: str
    unit_quantity: int
    unit_duration: int
    reminder_delay: int

    def __init__(self, props):
        self.id = props.get('id')
        self.name = props.get('name')
        self.description = props.get('description')
        self.unit_label = props.get('unit_label')
        self.unit_quantity = props.get('unit_quantity')
        self.unit_duration = props.get('unit_duration')
        self.reminder_delay = props.get('reminder_delay')

    @classmethod
    def validate_fields(self, data):
        mandatory_fields = ["name", "description", "unit_label", "unit_quantity", "unit_duration", "reminder_delay"]
        data_fields = data.keys()

        missing_fields = []

        for mandatory_field in mandatory_fields:
            if mandatory_field not in data_fields:
                missing_fields.append(mandatory_field)

        return missing_fields

    def to_dict(self):
        return dataclasses.asdict(self)