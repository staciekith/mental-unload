from typing import List
from app.domains.event_type import EventType

class ListEventTypes:
    def execute(repo, user) -> List[EventType]:
        event_types = repo.list(user)

        return {"ok": event_types}