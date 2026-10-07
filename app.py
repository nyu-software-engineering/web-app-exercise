import os
from datetime import datetime, timezone

import pymongo
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DBNAME")]
items = db.items

@app.route("/")
def home():
    recent = items.find().sort("created_at", pymongo.DESCENDING).limit(50)
    return render_template("index.html", items=list(recent))

@app.route("/db-test")
def db_test():
    db.test.insert_one({"message": "hello", "created_at": datetime.now(timezone.utc)})
    count = db.test.count_documents({})
    return f"Connected! test collection has {count} documents."

if __name__ == "__main__":
    app.run(port=8000, debug=True)