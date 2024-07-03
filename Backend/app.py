
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from events import add_event, remove_event, search_events, display_schedule
from participants import register_participant, remove_participant, display_participants
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/events/add', methods=['POST'])
def add_new_event():
    try:
        event_details = request.json
        add_event(event_details)
        return jsonify({"message": "Event added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/events/remove/<int:event_id>', methods=['DELETE'])
def remove_an_event(event_id):
    try:
        remove_event(event_id)
        return jsonify({"message": "Event removed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/events/search', methods=['GET'])
def search_events_endpoint():
    search_query = request.args.get('query')
    results = search_events(search_query)
    return jsonify(results)

@app.route('/participants/register/<int:event_id>', methods=['POST'])
def register_participant_endpoint(event_id):
    try:
        participant_details = request.json
        register_participant(event_id, participant_details)
        return jsonify({"message": "Participant registered successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/participants/remove/<int:event_id>/<int:participant_id>', methods=['DELETE'])
def remove_participant_endpoint(event_id, participant_id):
    try:
        remove_participant(event_id, participant_id)
        return jsonify({"message": "Participant removed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/participants/display/<int:event_id>', methods=['GET'])
def display_participants_endpoint(event_id):
    try:
        participants_list = display_participants(event_id)
        return jsonify(participants_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/schedule', methods=['GET'])
def display_schedule_endpoint():
    try:
        schedule = display_schedule()
        return jsonify(schedule)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
