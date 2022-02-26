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

    def __init__(self, props):
        self.id = props.get('id')
        self.title = props.get('title')
        self.quantity = props.get('quantity')
        self.done_at = props.get('done_at')
        self.due_at = props.get('due_at')
        self.remind_at = props.get('remind_at')
        self.status = props.get('status')
        self.type_id = props.get('type_id')

    @classmethod
    def validate_fields(self, data):
        mandatory_fields = ["title", "quantity", "type_id"]
        data_fields = data.keys()

        missing_fields = []

        for mandatory_field in mandatory_fields:
            if mandatory_field not in data_fields:
                missing_fields.append(mandatory_field)

        return missing_fields

    def to_dict(self):
        return dataclasses.asdict(self)