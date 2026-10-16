# Jobify

A little exercise to build a web application following an agile development process. See the [instructions](instructions.md) for more detail.

## Product vision statement

Jobify is a mobile web app that lets job seekers record, track and update every application they send out, keeping all the important information in one place.

## User stories

[User stories (Issues)](https://github.com/software-students-fall2026/web-app-exercise-LDJC/issues)

## Task boards

[Task boards (Projects)](https://github.com/software-students-fall2026/web-app-exercise-LDJC/projects)

## Steps necessary to run the software

### Prerequisites

- Python 3.9 or newer
- git

### 1. Clone the repository

```
git clone https://github.com/software-students-fall2026/web-app-exercise-LDJC.git
cd web-app-exercise-LDJC
```

### 2. Run the course setup script

Mac/Linux:
```
python3 .automations/setup.py
```
Windows:
```
python .automations/setup.py
```

### 3. Create and activate a virtual environment

Mac/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows (Command Prompt):
```
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Create the `.env` file

Copy the example file:

- Mac/Linux: `cp env.example .env`
- Windows: `copy env.example .env`

Then open `.env` and replace the dummy values with the real MongoDB connection string and database name. Team members and admins receive these in the team's messaging channel. Never commit `.env`.

### 6. Run the app

```
flask --app app run --debug
```

The terminal should print `* Connected to MongoDB!`. Open http://127.0.0.1:5000 in a browser. Use the browser's mobile view (developer tools → device toolbar) to see the intended phone layout.
