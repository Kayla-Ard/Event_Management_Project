
# empty dictionary to store events
events = {}

# Function to add a new event
def add_event(event_details):
    event_id = event_details['event_id']
    events[event_id] = event_details

# Function to remove an event
def remove_event(event_id):
    if event_id in events:
        del events[event_id]
    else:
        raise ValueError(f"Event with ID {event_id} not found.")

# Function to search for events by name, date, or location
def search_events(search_query):
    results = []
    for event_id, event_details in events.items():
        if search_query in event_details.values():
            results.append(event_details)
    return results
