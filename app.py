from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["webhooks"]
collection = db["events"]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Server started"})

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        if collection is None:
            raise RuntimeError("MongoDB not connected")

        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        event_type = data.get("event", "unknown")
        timestamp = data.get("timestamp", "unknown")
        author = data.get("author", "unknown")

        record = {
            "event": event_type,
            "author": author,
            "timestamp": timestamp
        }

        if event_type in ["PULL_REQUEST","MERGE"] :
            record["from_branch"] = data.get("from_branch", "unknown")
            record["to_branch"] = data.get("to_branch", "unknown")

        elif event_type == "PUSH":
            record["branch"] = data.get("branch", "unknown")

        collection.insert_one(record)
        return jsonify({"message": f"{event_type} event stored successfully"}), 200

    except Exception as e:
        print("Error in /webhook:", str(e))
        return jsonify({"error": "Webhook failed"}), 500

@app.route("/events", methods=["GET"])
def get_events():
    try:
        if collection is None:
            raise RuntimeError("MongoDB not connected")
        
        events = list(collection.find().sort("timestamp", -1))
        return dumps(events), 200

    except Exception as e:
        print("❌ Error in /events:", str(e))
        return jsonify({"error": "Could not fetch events"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
