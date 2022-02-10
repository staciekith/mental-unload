from typing import List
from app.domains.event_type import EventType

class ListEventTypes:
    def execute(repo) -> List[EventType]:
        event_types = repo.list()

        return event_types