from app import db

class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    done_at = db.Column(db.DateTime)
    due_at = db.Column(db.DateTime)
    remind_at = db.Column(db.DateTime)
    status = db.Column(db.String(), nullable=False, default='done')
    type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'), nullable=False)

    def __init__(self, props):
        self.title = props.title
        self.quantity = props.quantity
        self.done_at = props.done_at
        self.due_at = props.due_at
        self.remind_at = props.remind_at
        self.status = props.status
        self.type_id = props.type_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'quantity': self.quantity,
            'done_at': self.done_at,
            'due_at': self.due_at,
            'remind_at': self.remind_at,
            'status': self.status,
            'type_id': self.type_id
        }

    def create(event):
        db.session.add(event)
        db.session.commit()

        return event

    def update(event):
        db.session.commit()

        return event

    def delete(event):
        db.session.delete(event)
        db.session.commit()