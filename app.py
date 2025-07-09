from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.json_util import dumps 

import os


load_dotenv()

app = Flask(__name__)

CORS(app)


MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["webhooks"]
collection = db["events"]


@app.route("/",methods = ["GET"])
def hello():
    return jsonify({
        "message" : "Server started"
    })


@app.route("/webhook",methods = ["POST"])
def webhook():
    data = request.json

    event_type = data.get("event","unknown")
    timestamp = data.get("timestamp","unknown")
    author = data.get("author","unknown")
    record = {
        "event" : event_type,
        "author" : author,
        "timestamp" : timestamp
    }

    if event_type in ["PULL_REQUEST", "MERGE"]:
        record.update({ 
            "from_branch" : data.get("from_branch","unknown"),
            "to_branch" : data.get("to_branch","unknown"),
        })
    
    elif event_type == "PUSH": 
        record["branch"] = data.get("branch","unknown")   
    

    collection.insert_one(record)
    return jsonify({
        "message" : f"{event_type} event stored successfully"
    }),200

@app.route("/events",methods = ["GET"])

def get_events():
    events = list(collection.find().sort("timestamp",-1))
    print(events)
    return dumps(events),200

if __name__ == "__main__":
    app.run(port=5000,debug=True)



