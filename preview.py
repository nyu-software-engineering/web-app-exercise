
from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample data for frontend preview only
reports = [
    {
        "id": 1,
        "item": "AirPods Pro",
        "category": "Electronics",
        "type": "lost",
        "location": "Bobst Library",
        "date": "2026-10-18",
        "description": "White AirPods Pro with a pink case.",
        "contact": "example1@nyu.edu"
    },
    {
        "id": 2,
        "item": "Silver Keys",
        "category": "Keys",
        "type": "found",
        "location": "Paulson Center",
        "date": "2026-10-17",
        "description": "A set of silver keys found near the entrance.",
        "contact": "example2@nyu.edu"
    },
    {
        "id": 3,
        "item": "Black Jacket",
        "category": "Clothing",
        "type": "lost",
        "location": "Kimmel Center",
        "date": "2026-10-16",
        "description": "Black zip-up jacket, size medium.",
        "contact": "example3@nyu.edu"
    },
    {
        "id": 4,
        "item": "Purple Tote Bag",
        "category": "Accessories",
        "type": "found",
        "location": "Washington Square",
        "date": "2026-10-15",
        "description": "Purple canvas tote bag with books inside.",
        "contact": "example4@nyu.edu"
    }
]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report/lost")
def report_lost():
    return render_template("report_form.html", report_type="lost")


@app.route("/report/found")
def report_found():
    return render_template("report_form.html", report_type="found")


@app.route("/reports")
def browse_reports():
    return render_template("reports.html", reports=reports)


@app.route("/reports/<int:report_id>")
def report_detail(report_id):
    report = next(
        (r for r in reports if r["id"] == report_id),
        None
    )

    if report is None:
        abort(404)

    return render_template("report_detail.html", report=report)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
