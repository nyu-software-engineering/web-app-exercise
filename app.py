import os
from datetime import datetime, timezone

import pymongo
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DBNAME")]

@app.route("/")
def home():
    return "Campus Lost & Found"

@app.route("/db-test")
def db_test():
    db.test.insert_one({"message": "hello", "created_at": datetime.now(timezone.utc)})
    count = db.test.count_documents({})
    return f"Connected! test collection has {count} documents."

if __name__ == "__main__":
    app.run(port=8000, debug=True)