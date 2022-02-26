import pytest
import collections
from datetime import datetime
from app.adapters.postgres_database.repositories.event_repo import EventRepo
from app.adapters.postgres_database.models.event import Event
from app.adapters.postgres_database.models.event_type import EventType

@pytest.fixture(scope='function')
def init_db(app_db):
    app_db.create_all()

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

    event_2 = {
        'id': 2,
        'title': "event 2",
        'quantity': 1,
        'done_at': datetime.now(),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    app_db.session.add(EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values())))
    app_db.session.add(Event(collections.namedtuple("event", event_1.keys())(*event_1.values())))
    app_db.session.add(Event(collections.namedtuple("event", event_2.keys())(*event_2.values())))
    app_db.session.commit()

    yield

    app_db.drop_all()

def test_list(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        result = EventRepo.list()
        event = result[0]

    # THEN
    assert 2 == len(result)
    assert "event 1" == event.title

def test_find(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        existing_result = EventRepo.find(1)
        no_result = EventRepo.find(3)

    # THEN
    assert None != existing_result
    assert "event 1" == existing_result.title
    assert None == no_result

def test_create(app, init_db):
    # GIVEN
    event = {
        'title': "event created",
        'quantity': 1,
        'done_at': datetime.now(),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }
    event = Event(collections.namedtuple("event", event.keys())(*event.values()))

    # WHEN
    with app.app_context():
        created = EventRepo.create(event)

    # THEN
    assert None != created
    assert None != created.id
    assert "event created" == created.title

def test_update(app, init_db):
    # GIVEN
    event = {
        'id': 1,
        'title': "event updated",
        'quantity': 1,
        'done_at': datetime.now(),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }
    event = Event(collections.namedtuple("event", event.keys())(*event.values()))

    # WHEN
    with app.app_context():
        updated = EventRepo.update(1, event)
        refreshed_updated = EventRepo.find(1)

    # THEN
    assert None != updated
    assert 1 == updated.id
    assert "event updated" == updated.title

    assert None != refreshed_updated
    assert 1 == refreshed_updated.id
    assert "event updated" == refreshed_updated.title

def test_delete(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        before_delete = EventRepo.find(2)
        EventRepo.delete(2)
        after_delete = EventRepo.find(2)

    # THEN
    assert None != before_delete
    assert 2 == before_delete.id
    assert None == after_delete