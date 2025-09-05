# 📊 Expense Tracker

A simple and interactive **Expense Tracker** web application built with **Flask**, storing data in a CSV file. It features a clean UI and smooth animations using **GSAP**.
Track your spending, manage descriptions, and calculate totals — all from your browser.

---

## 🚀 Features

* ✅ Add, edit, and delete expenses
* ✅ Total expense calculation
* ✅ Data saved locally in `expenses.csv`
* ✅ Responsive UI with smooth animations
* ✅ Built with Flask, HTML/CSS, JavaScript, and GSAP

---

## 🗂️ Project Structure

```
project/
├── web/
│   ├── expense_tracker.py        # Flask backend
│   ├── templates/
│   │   ├── index.html            # Main page
│   │   └── edit.html             # Edit form page
│   └── static/
│       ├── css/
│       │   └── style.css         # CSS
│       └── js/
│           └── script.js         # GSAP animations
│
├── expenses.csv                  # Stored expenses (auto-created)
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS, JavaScript, GSAP
* **Storage**: CSV file (`expenses.csv`)

---

## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo/web
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate     # On macOS/Linux
   venv\Scripts\activate        # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r ../requirements.txt
   ```

4. **Run the app**

   ```bash
   python expense_tracker.py
   ```

   Open your browser and go to:

   ```
   http://localhost:5000
   ```

---

## 📦 Requirements

* Python 3.x
* Flask (`pip install flask`)

---

## ✍️ Author

Made by **\[Nishith]**

---

📄 License

This project is open-source. Feel free to use or modify it as needed.