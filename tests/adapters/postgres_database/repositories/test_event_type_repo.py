import pytest
import collections
from app.adapters.postgres_database.repositories.event_type_repo import EventTypeRepo
from app.adapters.postgres_database.models.event_type import EventType
import support.event_type_repo_data as data

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
        'reminder_delay': 24,
        'user': 'user1'
    }

    event_type_2 = {
        'id': 2,
        'name': "event type 2",
        'description': "event type 2",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user2'
    }

    event_type_3 = {
        'id': 3,
        'name': "event type 3",
        'description': "event type 3",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }

    app_db.session.add(EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values())))
    app_db.session.add(EventType(collections.namedtuple("event_type", event_type_2.keys())(*event_type_2.values())))
    app_db.session.add(EventType(collections.namedtuple("event_type", event_type_3.keys())(*event_type_3.values())))
    app_db.session.commit()

    yield

    app_db.drop_all()

def test_list(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        result = EventTypeRepo.list('user1')

    # THEN
    assert 2 == len(result)
    assert data.list_result() == result

def test_find(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        existing_result = EventTypeRepo.find(1)
        no_result = EventTypeRepo.find(4)

    # THEN
    assert data.find_result() == existing_result
    assert None == no_result

def test_create(app, init_db):
    # GIVEN
    event_type = {
        'name': "event type created",
        'description': "event type created",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }
    event_type = EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values()))

    # WHEN
    with app.app_context():
        created = EventTypeRepo.create(event_type)

    # THEN
    assert data.create_result() == created

def test_update(app, init_db):
    # GIVEN
    event_type = {
        'name': "event type updated",
        'description': "event type updated",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24,
        'user': 'user1'
    }
    event_type = EventType(collections.namedtuple("event_type", event_type.keys())(*event_type.values()))

    # WHEN
    with app.app_context():
        updated = EventTypeRepo.update(1, event_type)
        refreshed_updated = EventTypeRepo.find(1)

    # THEN
    assert data.update_result() == updated
    assert data.update_result() == refreshed_updated

def test_delete(app, init_db):
    # GIVEN/WHEN
    with app.app_context():
        before_delete = EventTypeRepo.find(2)
        deleted = EventTypeRepo.delete(2)
        after_delete = EventTypeRepo.find(2)

    # THEN
    assert data.delete_result() == before_delete
    assert data.delete_result() == deleted
    assert None == after_delete