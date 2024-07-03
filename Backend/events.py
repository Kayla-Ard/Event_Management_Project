from collections import deque

# empty dictionary to store events
events = {}
waitlists = {}

# add a new event
def add_event(event_details):
    event_id = event_details['event_id']
    events[event_id] = event_details
    waitlists[event_id] = deque()

# remove an event
def remove_event(event_id):
    if event_id in events:
        del events[event_id]
        del waitlists[event_id]
    else:
        raise ValueError(f"Event with ID {event_id} not found.")

# search for events by name, date, or location
def search_events(search_query):
    results = []
    for event_id, event_details in events.items():
        if search_query in event_details.values():
            results.append(event_details)
    return results

# display a schedule of all events sorted by date and time
def display_schedule():
    sorted_events = sorted(events.values(), key=lambda x: (x['event_date'], x['event_time']))
    return sorted_events

# add a participant to the waitlist
def add_to_waitlist(event_id, participant_details):
    if event_id in waitlists:
        waitlists[event_id].append(participant_details)
    else:
        raise ValueError(f"Event with ID {event_id} not found.")

# get the next participant from the waitlist
def get_next_from_waitlist(event_id):
    if event_id in waitlists and waitlists[event_id]:
        return waitlists[event_id].popleft()
    else:
        return None
