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
    def validate_fields(self, data):
        mandatory_fields = ["title", "quantity", "type_id"]
        data_fields = data.keys()

        missing_fields = []

        for mandatory_field in mandatory_fields:
            if mandatory_field not in data_fields:
                missing_fields.append(mandatory_field)

        return missing_fields

    @classmethod
    def from_dict(self, d):
        self.id = d.get('id')
        self.title = d.get('title')
        self.quantity = d.get('quantity')
        self.done_at = d.get('done_at')
        self.due_at = d.get('due_at')
        self.remind_at = d.get('remind_at')
        self.status = d.get('status')
        self.type_id = d.get('type_id')

        return self

    def to_dict(self):
        return dataclasses.asdict(self)