from app.use_cases.list_events import ListEvents
from app.use_cases.create_event import CreateEvent
from app.use_cases.update_event import UpdateEvent
import support.event_use_case_data as data
import json

def test_get_events(client, monkeypatch, auth):
    # GIVEN
    def use_case_return(_repo, _user):
        return data.list_result()

    monkeypatch.setattr(ListEvents, "execute", use_case_return)

    def map_function(event):
        res = event.to_dict()
        res['done_at'] = 'Thu, 10 Feb 2022 09:30:00 GMT'

        return res

    expected = list(map(map_function, data.list_result()["ok"]))

    # WHEN
    response = client.get("/events", headers={'Authorization': 'Bearer token'})

    # THEN
    assert 200 == response.status_code
    assert expected == response.json

def test_post_events(client, monkeypatch, auth):
    # GIVEN
    def use_case_return(_event_repo, _event_type_repo, _data):
        return data.create_result()

    monkeypatch.setattr(CreateEvent, "execute", use_case_return)

    params = {
        'title': "event created",
        'quantity': 2040,
        'type_id': 1
    }
    expected = data.create_result()["ok"].to_dict()
    expected['done_at'] = 'Thu, 10 Feb 2022 09:30:00 GMT'

    # WHEN
    response = client.post(
        "/events",
        data=json.dumps(params),
        content_type='application/json',
        headers={'Authorization': 'Bearer token'}
    )

    # THEN
    assert 201 == response.status_code
    assert expected == response.json

def test_post_events_with_missing_fields(client, monkeypatch, auth):
    # GIVEN
    params = {}
    expected = {
        'data': {
            'missing_fields': [
                'title',
                'quantity',
                'type_id'
            ]
        },
        'message': 'Some fields are missing.'
    }

    # WHEN
    response = client.post(
        "/events",
        data=json.dumps(params),
        content_type='application/json',
        headers={'Authorization': 'Bearer token'}
    )

    # THEN
    assert 400 == response.status_code
    assert expected == response.json

def test_put_event(client, monkeypatch, auth):
    # GIVEN
    def use_case_return(_repo, _id, _data):
        return data.update_result()

    monkeypatch.setattr(UpdateEvent, "execute", use_case_return)

    params = {
        'title': "event updated",
        'quantity': 1,
        'type_id': 1
    }
    expected = data.update_result()["ok"].to_dict()
    expected['done_at'] = 'Thu, 10 Feb 2022 09:30:00 GMT'

    # WHEN
    response = client.put(
        "/events/1",
        data=json.dumps(params),
        content_type='application/json',
        headers={'Authorization': 'Bearer token'}
    )

    # THEN
    assert 200 == response.status_code
    print(expected)
    print(response.json)
    assert expected == response.json