from app import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reminder_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(), nullable=False, default='pending')

    def __init__(self, props):
        self.title = props.title
        self.description = props.description
        self.due_date = props.due_date
        self.reminder_date = props.reminder_date
        self.status = props.status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'reminder_date': self.reminder_date,
            'status': self.status
        }