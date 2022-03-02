from app.use_cases.create_event import CreateEvent
from app.domains.event import Event
import support.event_repo_data as event_repo_data
import support.event_type_repo_data as event_type_repo_data
import support.event_use_case_data as data
from unittest.mock import Mock, call, patch
from datetime import datetime

def test_execute():
    # GIVEN
    params = {
        'title': "event created",
        'quantity': 2040,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1,
        'user': 'user1'
    }

    expected_repo_param = Event(params)

    reminder_params = {
        'title': "Reminder for event type 1",
        'quantity': 0,
        'done_at': None,
        'due_at': datetime(2022, 2, 16, 3, 0, 0, 0),
        'remind_at': datetime(2022, 2, 15, 3, 0, 0, 0),
        'status': "pending",
        'type_id': 1,
        'user': 'user1'
    }

    expected_reminder_repo_param = Event(reminder_params)

    event_type_repo_mock = Mock()
    event_type_repo_mock.find.return_value = event_type_repo_data.find_result()

    event_repo_mock = Mock()
    event_repo_mock.create.return_value = event_repo_data.create_result()

    # WHEN
    with patch('app.use_cases.create_event.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2022, 2, 10, 9, 30, 0, 0)
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

        result = CreateEvent.execute(event_repo_mock, event_type_repo_mock, params)

    # THEN
    event_type_repo_mock.find.assert_called_once()
    event_type_repo_mock.find.assert_called_once_with(1)

    event_repo_mock.create.assert_has_calls([call(expected_repo_param), call(expected_reminder_repo_param)])

    assert data.create_result() == result

def execute_when_event_type_not_found():
    # GIVEN
    params = {
        'title': "event created",
        'quantity': 2040,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 6,
        'user': 'user1'
    }

    event_type_repo_mock = Mock()
    event_type_repo_mock.find.return_value = None

    event_repo_mock = Mock()

    # WHEN
    result = CreateEvent.execute(event_repo_mock, event_type_repo_mock, params)

    # THEN
    event_type_repo_mock.find.assert_called_once()
    event_type_repo_mock.find.assert_called_once_with(1)

    event_repo_mock.create.assert_not_called()

    assert data.event_type_not_found_result(6) == result