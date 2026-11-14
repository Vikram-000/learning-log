from pydantic import BaseModel, Field, ValidationError

class Event(BaseModel):
    event_id : str = Field(min_length= 5, max_length=30)
    event_type : str = Field(min_length= 5, max_length=30)
    task_id : str = Field(min_length= 5, max_length=30)
    status : str = Field(min_length= 3, max_length=15)
    retry_count : int = Field(default=0, ge=0, le=10)

event = {
    "event_id": "",
    "event_type": "something_random",
    "task_id": "a",
    "status": "running",
    "retry_count": -50
}

event_1 = {
    "event_id": "evt_001",
    "event_type": "task_started",
    "task_id": "task_123",
    "status": "running",
    "retry_count": 2
}

event_2 = {
    "event_id": "evt_002",
    "event_type": "task_completed",
    "task_id": "task_123",
    "status": "success"
}

def create_event(event_data: Event):
    
    print("Event created successfully")

    return event_data


events = [event, event_1, event_2]

for event in events:
    try:
        event_data = Event.model_validate(event)
        validated_event = create_event(event_data)
        print(validated_event)

    except ValidationError as val_err:
        for err in val_err.errors():
            print(err["msg"])