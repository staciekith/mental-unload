from app import db

class EventType(db.Model):
    __tablename__ = 'event_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text)
    unit_label = db.Column(db.String(), nullable=False)
    unit_quantity = db.Column(db.Integer, nullable=False)
    unit_duration = db.Column(db.Integer, nullable=False)
    reminder_delay = db.Column(db.Integer, nullable=False)

    def __init__(self, props):
        self.name = props.name
        self.description = props.description
        self.unit_label = props.unit_label
        self.unit_quantity = props.unit_quantity
        self.unit_duration = props.unit_duration
        self.reminder_delay = props.reminder_delay

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'unit_label': self.unit_label,
            'unit_quantity': self.unit_quantity,
            'unit_duration': self.unit_duration,
            'reminder_delay': self.reminder_delay
        }

    def create(event_type):
        db.session.add(event_type)
        db.session.commit()

        return event_type