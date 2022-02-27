from app.use_cases.list_event_types import ListEventTypes
import support.event_type_repo_data as repo_data
import support.event_type_use_case_data as data
from unittest.mock import Mock

def test_execute():
    # GIVEN
    repo_mock = Mock()
    repo_mock.list.return_value = repo_data.list_result()

    # WHEN
    result = ListEventTypes.execute(repo_mock)

    # THEN
    repo_mock.list.assert_called_once()
    assert data.list_result() == result
