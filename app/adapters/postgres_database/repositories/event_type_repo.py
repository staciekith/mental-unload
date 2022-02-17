from typing import List
from app.domains.event_type import EventType
from app.adapters.postgres_database.models import EventType as EventTypeModel

class EventTypeRepo:
    def list(filters = None) -> List[EventType]:
        results = EventTypeModel.query.all()

        return [EventType(**row.serialize()) for row in results]

    def find(event_type_id: int) -> EventType:
        event_type_model = EventTypeModel.query.get(event_type_id)

        return EventType(**event_type_model.serialize())

    def create(event_type: EventType) -> EventType:
        event_type_model = EventTypeModel(event_type)
        created_event_type = EventTypeModel.create(event_type_model)

        event_type_model.id = created_event_type.id

        return EventType(**event_type_model.serialize())

    def update(event_type_id: int, event_type: EventType) -> EventType:
        event_type_to_update = EventTypeModel.query.get(event_type_id)

        if (event_type_to_update):
            event_type_to_update.name = event_type.name
            event_type_to_update.description = event_type.description
            event_type_to_update.unit_label = event_type.unit_label
            event_type_to_update.unit_quantity = event_type.unit_quantity
            event_type_to_update.unit_duration = event_type.unit_duration
            event_type_to_update.reminder_delay = event_type.reminder_delay

            EventTypeModel.update(event_type_to_update)

        return EventType(**event_type_to_update.serialize())

    def delete(event_type_id: int) -> None:
        event_type_to_delete = EventTypeModel.query.get(event_type_id)

        if (event_type_to_delete):
            EventTypeModel.delete(event_type_to_delete)
