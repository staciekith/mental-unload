from app.use_cases.update_event_type import UpdateEventType
from app.domains.event_type import EventType
import support.event_type_repo_data as repo_data
from unittest.mock import Mock

def test_execute():
    # GIVEN
    data = {
        'id': 1,
        'name': "event type updated",
        'description': "event type updated",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    expected_repo_param = EventType(data)

    repo_mock = Mock()
    repo_mock.find.return_value = repo_data.find_result()
    repo_mock.update.return_value = repo_data.update_result()

    # WHEN
    result = UpdateEventType.execute(repo_mock, 1, data)

    # THEN
    repo_mock.find.assert_called_once()
    repo_mock.find.assert_called_once_with(1)
    repo_mock.update.assert_called_once()
    repo_mock.update.assert_called_once_with(1, expected_repo_param)
    assert {'ok': repo_data.update_result()} == result

def test_execute_when_not_found():
    # GIVEN
    data = {
        'id': 6,
        'name': "event type updated",
        'description': "event type updated",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    repo_mock = Mock()
    repo_mock.find.return_value = None

    # WHEN
    result = UpdateEventType.execute(repo_mock, 6, data)

    # THEN
    repo_mock.find.assert_called_once()
    repo_mock.find.assert_called_once_with(6)
    repo_mock.update.assert_not_called()
    assert {'error': "EventType with ID 6 does not exist"} == result