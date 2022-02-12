from typing import List
from app.domains.event import Event

class ListEvents:
    def execute(repo) -> List[Event]:
        events = repo.list()

        return events