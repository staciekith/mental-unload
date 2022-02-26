import pytest
import collections
from datetime import datetime
from app.adapters.postgres_database.repositories.event_repo import EventRepo
from app.adapters.postgres_database.models.event import Event
from app.adapters.postgres_database.models.event_type import EventType

@pytest.fixture(scope='module')
def init_db(app_db):
    event_type = {
        'id': 1,
        'name': "event type 1",
        'description': "event type 1",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    event_1 = {
        'id': 1,
        'title': "event 1",
        'quantity': 1,
        'done_at': datetime.now(),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    app_db.session.add(EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values())))
    app_db.session.add(Event(collections.namedtuple("event", event_1.keys())(*event_1.values())))
    app_db.session.commit()

    yield

    app_db.drop_all()

def test_list(app, init_db):
    with app.app_context():
        assert 1 == len(EventRepo.list())
