from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('doctor_availability.db')
c = conn.cursor()

# Dummy data for doctor availability
doctor_availability = {
    "1": ["10:00 AM", "02:00 PM", "04:00 PM"]
}

@app.route('/api/doctor_availability', methods=['GET'])
def get_doctor_availability():
    doctor_id = request.args.get('doctor_id')
    if doctor_id in doctor_availability:
        return jsonify({"doctor_id": doctor_id, "availability": doctor_availability[doctor_id]})
    else:
        return jsonify({"error": "Doctor not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
