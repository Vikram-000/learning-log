from pydantic import BaseModel, Field, ValidationError, ConfigDict
from typing import Dict, List, Any

class Events(BaseModel):
    model_config = ConfigDict(validated_default = True)
    event_id : str = Field(min_length= 5, max_length=30)
    event_type : str = Field(min_length= 5, max_length=30)
    description : str | None = Field(default= None, min_length= 5, max_length=30)
    metadata : Dict[str, Any] = Field(default_factory= dict)  
    tags : List[str] = Field(default_factory= list, min_length= 2, max_length=10)

event_1 = {
    "event_id": "EVT001",
    "event_type": "conference",
    "description": "Annual technology conference",
    "metadata": {
        "location": "Pune",
        "organizer": "Tech Events India"
    },
    "tags": ["technology", "networking", "conference"]
}

event_2 = {
    "event_id": "EVT002",
    "event_type": "workshop"
}
event_3 = {
    "event_id": "EVT002",
    "event_type": "workshop",
    "description" : None,
    "metadata" : None
}


def create_event(events: Events):
    print("Event created successfully")
    return events

events = [event_1, event_2, event_3]

for event in events:
    try:
        event_data = Events.model_validate(event)
        validated_event = create_event(event_data)
        print(validated_event)

    except ValidationError as val_err:
        for err in val_err.errors():
            print(err["msg"])