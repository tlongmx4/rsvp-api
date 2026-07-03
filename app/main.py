from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

events = {}
next_id = 1

class EventPayload(BaseModel):
    name: str
    date: str
    capacity: int

class MakeRSVP(BaseModel):
    name: str
    response: str

class RSVPStatus(str, Enum):
    YES = "yes",
    NO = "no",
    MAYBE = "maybe"

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
        "capacity": event.capacity,
        "attendees": {}
    }

    events[assigned_id] = new_event_record

    return(new_event_record)


@app.get("/events/{id}")
def get_event(id: int):
    if id in events:
        return events[id]
    else:
        raise HTTPException(status_code=404, detail="Event not found")
    
@app.post("/events/{id}/rsvp")
def make_rsvp(id: int, payload: MakeRSVP):
    if id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    
    target_event=events[id]

    if "attendees" not in target_event:
        target_event["attendees"] = {}

    target_event["attendees"][payload.name] = payload.response

    return target_event

@app.get("/events/{id}/attendees")
def find_attendees(id: int):
    if id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    return events[id]["attendees"]