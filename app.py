from flask import Flask, request, jsonify
import pytz
from datetime import datetime
from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv
from flask_cors import CORS
import os


port = int(os.environ.get("PORT", 5000))

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

        event_type = request.headers.get("X-GitHub-Event", "unknown")
        author = data.get("sender", {}).get("login", "unknown")
        timestamp = data.get("repository", {}).get("pushed_at", "unknown") 
        pr = data.get("pull_request", {})

        utc_time_str = pr.get("updated_at") if event_type == "pull_request" else data.get("repository", {}).get("pushed_at")

        if utc_time_str:
            utc_dt = (
                datetime.utcfromtimestamp(utc_time_str)
                if isinstance(utc_time_str, int)
                else datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%SZ")
            )
            ist = pytz.timezone("Asia/Kolkata")
            ist_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(ist)
            timestamp = ist_dt.strftime("%d %B %Y - %I:%M %p IST")
        else:
            timestamp = "unknown"

        record = {
            "event": event_type.upper(),
            "author": author,
            "timestamp": timestamp
        }

        if event_type == "push":
             record["to_branch"] = data.get("ref", "unknown").split("/")[-1]

        elif event_type == "pull_request":
           
            record["from_branch"] = pr.get("head", {}).get("ref", "unknown")
            record["to_branch"] = pr.get("base", {}).get("ref", "unknown")

        elif event_type == "merge_group":  # Optional
            record["from_branch"] = data.get("head_ref", "unknown")
            record["to_branch"] = data.get("base_ref", "unknown")

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
        print("Error in /events:", str(e))
        return jsonify({"error": "Could not fetch events"}), 500
    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
