# Event RSVP API

A REST API for events and RSVPs. Built with FastAPI.
An event is created and returns an ID. The ID is used to find an event and RSVP.
The ID can also be used to check who has RSVP'd to the event.

## What this demonstrates

This project is focused on backend skills only.
It shows API design, data modeling, and correctness handling.

## Tech stack

- Python
- FastAPI
- In-memory storage for now

## Design decisions

- Attendees are stored as a map keyed by username, so each person can only have one RSVP. A duplicate or conflicting response overwrites the old one instead of creating a second entry.
- RSVP status is an enum, so only yes/no/maybe are accepted. Any other value is rejected before it reaches the logic.

## Running it

Run the server:

​```bash
uvicorn app.main:app --reload
​```

Interactive docs are available at http://127.0.0.1:8000/docs

## Planned / next steps

- Capacity enforcement (reject RSVPs once an event is full)
- Thread-safety for the capacity check
- Persistence with PostgreSQL + SQLAlchemy
- Invitation based RSVP