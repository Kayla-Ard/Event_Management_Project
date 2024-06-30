# Event Management System

This project is a dynamic event management system built using Python and Flask.

## Features

- Add, remove, and search events.
- Register and manage participants for each event.
- Display schedules and handle wait-lists.


## API Endpoints

- POST /events/add: Add a new event.
- DELETE /events/remove/<event_id>: Remove an event by ID.
- GET /events/search?query=<search_query>: Search for events by name, date, or location.
- POST /participants/register/<event_id>: Register a participant for an event.
- DELETE /participants/remove/<event_id>/<participant_id>: Remove a participant from an event.
- GET /participants/display/<event_id>: Display participants for an event.


