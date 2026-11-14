from pydantic import BaseModel

class ExecutionEvent(BaseModel):
    event_id : str
    event_type : str 
    task_id : str 
    status : str
    retry_count : int = 0

event_1 = {
    "event_id": "evt_001",
    "event_type": "task_started",
    "task_id": "task_123",
    "status": "running",
    "retry_count": 0
}

event_2 = {
    "event_id": "evt_002",
    "event_type": "task_completed",
    "task_id": "task_123",
    "status": "success"
}


def create_event(event_data: ExecutionEvent):
    
    print("Event created successfully")

    return event_data

event_data = ExecutionEvent.model_validate(event_2)

validated_event = create_event(event_data)

print(validated_event)
