from app.use_cases.list_events import ListEvents
import support.event_repo_data as repo_data
import support.event_use_case_data as data
from unittest.mock import Mock

def test_execute():
    # GIVEN
    repo_mock = Mock()
    repo_mock.list.return_value = repo_data.list_result()

    # WHEN
    result = ListEvents.execute(repo_mock, 'user1')

    # THEN
    repo_mock.list.assert_called_once()
    assert data.list_result() == result
