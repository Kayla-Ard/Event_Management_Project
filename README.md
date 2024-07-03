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
- GET /schedule: Display a schedule of all events.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/Kayla-Ard/Event_Management_Project
    cd event-management-system
    ```

2. Install the required dependencies:
    ```bash
    pip install flask flask-cors
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your web browser and navigate to `http://localhost:5000` to view the frontend.

## Usage

- Use the frontend form to add new events.
- Use the provided API endpoints to manage events and participants.


