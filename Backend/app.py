
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from events import add_event, remove_event, search_events
from participants import register_participant, remove_participant, display_participants
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app, resources={r"/*": {"origins": "*"}})

# for the index.html file
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# add a new event
@app.route('/events/add', methods=['POST'])
@cross_origin()
def add_new_event():
    try:
        event_details = request.json
        add_event(event_details)
        return jsonify({"message": "Event added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# remove an event
@app.route('/events/remove/<int:event_id>', methods=['DELETE'])
@cross_origin()
def remove_an_event(event_id):
    try:
        remove_event(event_id)
        return jsonify({"message": "Event removed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# search for events
@app.route('/events/search', methods=['GET'])
@cross_origin()
def search_events_endpoint():
    search_query = request.args.get('query')
    results = search_events(search_query)
    return jsonify(results)

# register a participant for an event
@app.route('/participants/register/<int:event_id>', methods=['POST'])
@cross_origin()
def register_participant_endpoint(event_id):
    try:
        participant_details = request.json
        register_participant(event_id, participant_details)
        return jsonify({"message": "Participant registered successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# remove a participant from an event
@app.route('/participants/remove/<int:event_id>/<int:participant_id>', methods=['DELETE'])
@cross_origin()
def remove_participant_endpoint(event_id, participant_id):
    try:
        remove_participant(event_id, participant_id)
        return jsonify({"message": "Participant removed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# display participants for an event
@app.route('/participants/display/<int:event_id>', methods=['GET'])
@cross_origin()
def display_participants_endpoint(event_id):
    try:
        participants_list = display_participants(event_id)
        return jsonify(participants_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
