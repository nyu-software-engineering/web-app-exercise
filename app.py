import os

import pymongo
from dotenv import load_dotenv
from flask import Flask, render_template

from constants import BUILDINGS, CATEGORIES, ITEM_TYPES, STATUSES

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DBNAME")]
items = db.items

@app.context_processor
def inject_constants():
    """Make the dropdown lists available in every template."""
    return {
        "ITEM_TYPES": ITEM_TYPES,
        "STATUSES": STATUSES,
        "CATEGORIES": CATEGORIES,
        "BUILDINGS": BUILDINGS,
    }

@app.route("/")
def home():
    recent = items.find().sort("created_at", pymongo.DESCENDING).limit(50)
    return render_template("index.html", items=list(recent))

if __name__ == "__main__":
    app.run(port=8000, debug=True)