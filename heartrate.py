from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)
json_file_path = "heart_records.json"

@app.route('/insert_heart_record', methods=['POST'])
def insert_heart_record():
    data = request.get_json()

    
    heart_id = data.get('heart_id')
    date_str = data.get('date')
    heart_rate = data.get('heart_rate')
    new_record = {
        "heart_id": heart_id,
        "date": date.strftime("%Y-%m-%d"),
        "heart_rate": heart_rate
    }

    
    heart_records.append(new_record)

    
    with open(json_file_path, "w") as file:
        json.dump(heart_records, file, indent=2)

    return jsonify({"message": "Heart record added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
