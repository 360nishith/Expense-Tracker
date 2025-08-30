Expense Tracker

A simple expense tracking project with two versions:

CLI Version — A command-line app to log and view expenses.

Web App Version — A Flask-based web interface to manage expenses in the browser.

Project Structure

project/
├── cli/
│ └── expense_tracker.py

├── web/
│ ├── expense_tracker.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── js/
│ └── script.js

├── expenses.txt
├── requirements.txt
├── .gitignore
└── README.md

Requirements

Python 3.x

Flask (for the web version)

Install dependencies with:

pip install -r requirements.txt

CLI Version

How to Run:

cd cli
python expense_tracker.py

Features:

Add expenses with amount and description

View all expenses with numbering

Stores data in expenses.txt (shared with web app)

Web App Version

How to Run:

cd web
python expense_tracker.py

Then open your browser and go to:

http://localhost:5000

Features:

Add and view expenses through a browser

Clean UI with HTML + JavaScript

Data saved in shared expenses.txt

Note

To protect local data, expenses.txt is listed in .gitignore and will not be pushed to GitHub.

Future Plans

Add animations using GSAP (next commit)

Add delete/edit functionality

Author

Made by [Nishith]