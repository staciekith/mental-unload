from datetime import datetime
from app.use_cases.update_event import UpdateEvent
from app.domains.event import Event
import support.event_repo_data as repo_data
import support.event_use_case_data as data
from unittest.mock import Mock

def test_execute():
    # GIVEN
    params = {
        'id': 1,
        'title': "event updated",
        'quantity': 1,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    expected_repo_param = Event(params)
    expected_repo_param.user = 'user1'

    repo_mock = Mock()
    repo_mock.find.return_value = repo_data.find_result()
    repo_mock.update.return_value = repo_data.update_result()

    # WHEN
    result = UpdateEvent.execute(repo_mock, 1, params)

    # THEN
    repo_mock.find.assert_called_once()
    repo_mock.find.assert_called_once_with(1)
    repo_mock.update.assert_called_once()
    repo_mock.update.assert_called_once_with(1, expected_repo_param)
    assert data.update_result() == result

def test_execute_when_not_found():
    # GIVEN
    params = {
        'id': 6,
        'title': "event updated",
        'quantity': 1,
        'done_at': datetime(2022, 2, 10, 9, 30, 0, 0),
        'due_at': None,
        'remind_at': None,
        'status': "done",
        'type_id': 1
    }

    repo_mock = Mock()
    repo_mock.find.return_value = None

    # WHEN
    result = UpdateEvent.execute(repo_mock, 6, params)

    # THEN
    repo_mock.find.assert_called_once()
    repo_mock.find.assert_called_once_with(6)
    repo_mock.update.assert_not_called()
    assert data.not_found_result(6) == result