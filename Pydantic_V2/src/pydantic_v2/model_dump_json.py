from pydantic import BaseModel

class Event(BaseModel):
    event_id : str
    event_type : str 
    task_id : str 
    status : str
    retry_count : int = 0

event = {
    "event_id": "evt_001",
    "event_type": "task_started",
    "task_id": "task_123",
    "status": "running",
    "retry_count": 0
}

def create_event(event_data: Event):
    
    print("Event created successfully")

    json_data = event_data.model_dump_json(indent=2)
    with open("event.json", "w") as f:
        f.write(json_data)

    return event_data

event_data = Event.model_validate(event)

validated_event = create_event(event_data)

print(validated_event)