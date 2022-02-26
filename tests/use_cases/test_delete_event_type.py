from app.use_cases.delete_event_type import DeleteEventType
import support.event_type_repo_data as repo_data
from unittest.mock import Mock

def test_execute():
    # GIVEN
    repo_mock = Mock()
    repo_mock.find.return_value = repo_data.find_result()
    repo_mock.delete.return_value = repo_data.delete_result()

    # WHEN
    result = DeleteEventType.execute(repo_mock, 2)

    # THEN
    repo_mock.find.assert_called_once()
    repo_mock.find.assert_called_once_with(2)
    repo_mock.delete.assert_called_once()
    repo_mock.delete.assert_called_once_with(2)
    assert {'ok': repo_data.delete_result()} == result

def test_execute_when_not_found():
    # GIVEN
    repo_mock = Mock()
    repo_mock.find.return_value = None

    # WHEN
    result = DeleteEventType.execute(repo_mock, 6)

    # THEN
    repo_mock.find.assert_called_once()
    repo_mock.find.assert_called_once_with(6)
    repo_mock.delete.assert_not_called()
    assert {'error': "EventType with ID 6 does not exist"} == result