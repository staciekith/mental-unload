from typing import List
from app.domains.event import Event

class ListEvents:
    def execute(repo, user) -> List[Event]:
        events = repo.list(user)

        return {"ok": events}