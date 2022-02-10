from typing import List
from app.domains.event_type import EventType
from app.adapters.postgres_database.models import EventType as EventTypeModel

class EventTypeRepo:
    def list(filters = None) -> List[EventType]:
        results = EventTypeModel.query.all()

        return [EventType(**row.serialize()) for row in results]

