from app.use_cases.create_event_type import CreateEventType
from app.domains.event_type import EventType
import support.event_type_repo_data as repo_data
from unittest.mock import Mock

def test_execute():
    # GIVEN
    data = {
        'name': "event type created",
        'description': "event type created",
        'unit_label': "g",
        'unit_quantity': 170,
        'unit_duration': 12,
        'reminder_delay': 24
    }

    expected_repo_param = EventType(data)

    repo_mock = Mock()
    repo_mock.create.return_value = repo_data.create_result()

    # WHEN
    result = CreateEventType.execute(repo_mock, data)

    # THEN
    repo_mock.create.assert_called_once()
    repo_mock.create.assert_called_once_with(expected_repo_param)
    assert {'ok': repo_data.create_result()} == result
