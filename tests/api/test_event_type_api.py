from app.use_cases.list_event_types import ListEventTypes
from app.use_cases.create_event_type import CreateEventType
from app.use_cases.update_event_type import UpdateEventType
import support.event_type_use_case_data as data
import json

def test_get_event_types(client, monkeypatch, auth):
    # GIVEN
    def use_case_return(_repo, _user):
        return data.list_result()

    monkeypatch.setattr(ListEventTypes, "execute", use_case_return)

    expected = list(map(lambda event_type: event_type.to_dict(), data.list_result()["ok"]))

    # WHEN
    response = client.get("/event_types", headers={'Authorization': 'Bearer token'})

    # THEN
    assert 200 == response.status_code
    assert expected == response.json

def test_post_event_types(client, monkeypatch, auth):
    # GIVEN
    def use_case_return(_repo, _data):
        return data.create_result()

    monkeypatch.setattr(CreateEventType, "execute", use_case_return)

    params = {
        'name': "event type created",
        'description': "event type created",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }
    expected = data.create_result()["ok"].to_dict()

    # WHEN
    response = client.post(
        "/event_types",
        data=json.dumps(params),
        content_type='application/json',
        headers={'Authorization': 'Bearer token'}
    )

    # THEN
    assert 201 == response.status_code
    assert expected == response.json

def test_post_event_types_with_missing_fields(client, monkeypatch, auth):
    # GIVEN
    params = {}
    expected = {
        'data': {
            'missing_fields': [
                'name',
                'description',
                'unit_label',
                'unit_quantity',
                'unit_duration',
                'reminder_delay'
            ]
        },
        'message': 'Some fields are missing.'
    }

    # WHEN
    response = client.post(
        "/event_types",
        data=json.dumps(params),
        content_type='application/json',
        headers={'Authorization': 'Bearer token'}
    )

    # THEN
    assert 400 == response.status_code
    assert expected == response.json

def test_put_event_type(client, monkeypatch, auth):
    # GIVEN
    def use_case_return(_repo, _id, _data):
        return data.update_result()

    monkeypatch.setattr(UpdateEventType, "execute", use_case_return)

    params = {
        'name': "event type created",
        'description': "event type created",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }
    expected = data.update_result()["ok"].to_dict()

    # WHEN
    response = client.put(
        "/event_types/1",
        data=json.dumps(params),
        content_type='application/json',
        headers={'Authorization': 'Bearer token'}
    )

    # THEN
    assert 200 == response.status_code
    assert expected == response.json