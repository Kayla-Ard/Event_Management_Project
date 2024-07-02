
# empty dictionary to store participants by event ID
participants = {}

# register a participant for an event
def register_participant(event_id, participant_details):
    if event_id in participants:
        if len(participants[event_id]) >= events[event_id]['participant_limit']:
            raise ValueError("Participant limit exceeded for this event.")
        participants[event_id].append(participant_details)
    else:
        raise ValueError(f"Event with ID {event_id} not found.")

# remove a participant from an event
def remove_participant(event_id, participant_id):
    if event_id in participants:
        for participant in participants[event_id]:
            if participant['participant_id'] == participant_id:
                participants[event_id].remove(participant)
                return
        raise ValueError(f"Participant with ID {participant_id} not found for event {event_id}.")
    else:
        raise ValueError(f"Event with ID {event_id} not found.")

# display participants for an event
def display_participants(event_id):
    if event_id in participants:
        return participants[event_id]
    else:
        raise ValueError(f"Event with ID {event_id} not found.")
