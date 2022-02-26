import pytest
import collections
from datetime import datetime
from app.adapters.postgres_database.repositories.event_type_repo import EventTypeRepo
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

    event_type_2 = {
        'id': 2,
        'name': "event type 2",
        'description': "event type 2",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    app_db.session.add(EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values())))
    app_db.session.add(EventType(collections.namedtuple("event_type", event_type_2.keys())(*event_type_2.values())))
    app_db.session.commit()

    yield

    app_db.drop_all()

def test_list(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        result = EventTypeRepo.list()
        event_type = result[0]

    # THEN
    assert 2 == len(result)
    assert "event type 1" == event_type.name

def test_find(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        existing_result = EventTypeRepo.find(1)
        no_result = EventTypeRepo.find(3)

    # THEN
    assert None != existing_result
    assert "event type 1" == existing_result.name
    assert None == no_result

def test_create(app, init_db):
    # GIVEN
    event_type = {
        'name': "event type created",
        'description': "event type created",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }
    event_type = EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values()))

    # WHEN
    with app.app_context():
        created = EventTypeRepo.create(event_type)

    # THEN
    assert None != created
    assert None != created.id
    assert "event type created" == created.name

def test_update(app, init_db):
    # GIVEN
    event_type = {
        'name': "event type updated",
        'description': "event type updated",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }
    event_type = EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values()))

    # WHEN
    with app.app_context():
        updated = EventTypeRepo.update(1, event_type)
        refreshed_updated = EventTypeRepo.find(1)

    # THEN
    assert None != updated
    assert 1 == updated.id
    assert "event type updated" == updated.name

    assert None != refreshed_updated
    assert 1 == refreshed_updated.id
    assert "event type updated" == refreshed_updated.name

def test_delete(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        before_delete = EventTypeRepo.find(2)
        EventTypeRepo.delete(2)
        after_delete = EventTypeRepo.find(2)

    # THEN
    assert None != before_delete
    assert 2 == before_delete.id
    assert None == after_delete