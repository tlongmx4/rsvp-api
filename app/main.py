from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

events = {}
next_id = 1

class EventPayload(BaseModel):
    name: str
    date: str
    capacity: int

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/events")
def create_event(event: EventPayload):
    global next_id

    assigned_id = next_id
    next_id += 1

    new_event_record = {
        "id": assigned_id,
        "name": event.name,
        "date": event.date,
        "capacity": event.capacity
    }

    events[assigned_id] = new_event_record

    return(new_event_record)


@app.get("/events/{id}")
def get_event(id: int):
    if id in events:
        return events[id]
    else:
        raise HTTPException(status_code=404, detail="Event not found")