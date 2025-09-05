
---

## ✅ Final Version: `web/expense_tracker.py`

```python
from flask import Flask, render_template, request, redirect, flash
import csv
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Secret key for flash messages and session security

CSV_FILE = "expenses.csv"  # File to store expenses data
expenses = []  # In-memory list to hold expenses as tuples (amount, description)

# Function to load all expenses from CSV file into memory
def load_expenses():
    expenses.clear()  # Clear existing list to avoid duplicates on reload
    if os.path.exists(CSV_FILE):  # Check if CSV file exists
        with open(CSV_FILE, mode="r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                # Make sure each row has exactly 2 items: amount and description
                if len(row) == 2:
                    amount, description = row
                    # Append tuple (float amount, description string)
                    expenses.append((float(amount), description))

# Function to save all in-memory expenses back to the CSV file (overwrite)
def save_all_expenses():
    with open(CSV_FILE, mode="w", newline='') as file:
        writer = csv.writer(file)
        for amount, description in expenses:
            writer.writerow([amount, description])  # Write each expense as a CSV row

# Function to append a single new expense both to CSV file and in-memory list
def add_expense(amount, description):
    with open(CSV_FILE, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, description])  # Append new row to CSV
    expenses.append((float(amount), description))  # Also add to in-memory list

# Route: Homepage - Display form and list of expenses
@app.route("/")
def index():
    load_expenses()  # Reload data from CSV to sync with file
    total = sum(amount for amount, _ in expenses)
    expenses_with_index = [(amount, desc, idx) for idx, (amount, desc) in enumerate(expenses)]
    return render_template("index.html", expenses=expenses_with_index, total=total)

# Route: Handle adding a new expense via POST form
@app.route("/add", methods=["POST"])
def add():
    amount = request.form.get("amount")  # Retrieve amount from form data
    description = request.form.get("description")  # Retrieve description from form
    if amount and description:
        add_expense(amount, description)  # Add expense (both CSV & in-memory)
        flash("Expense added successfully!")  # Flash success message
    return redirect("/")  # Redirect back to homepage

# Route: Edit an expense by index (GET shows form, POST updates data)
@app.route("/edit/<int:idx>", methods=["GET", "POST"])
def edit(idx):
    load_expenses()  # Reload data for consistency

    # Validate index range
    if idx < 0 or idx >= len(expenses):
        flash("Invalid expense selected.")  # Flash error if invalid
        return redirect("/")

    if request.method == "POST":
        # Process the submitted form data to update expense
        new_amount = float(request.form.get("amount"))
        new_description = request.form.get("description")
        expenses[idx] = (new_amount, new_description)  # Update in-memory list
        save_all_expenses()  # Save changes to CSV file
        flash("Expense updated successfully!")  # Flash success message
        return redirect("/")

    # If GET request, show the form with existing expense data pre-filled
    amount, description = expenses[idx]
    return render_template("edit.html", amount=amount, description=description, idx=idx)

# Route: Delete an expense by index
@app.route("/delete/<int:idx>")
def delete(idx):
    load_expenses()  # Reload current data

    if idx < 0 or idx >= len(expenses):
        flash("Invalid expense selected.")  # Flash error if invalid
        return redirect("/")

    removed = expenses.pop(idx)  # Remove expense from in-memory list
    save_all_expenses()  # Save updated list to CSV
    flash(f"Deleted expense: ₹{removed[0]} - {removed[1]}")  # Flash which was deleted
    return redirect("/")

# Entry point to start the Flask application
if __name__ == "__main__":
    load_expenses()  # Load expenses before starting the server
    app.run(debug=True)  # Run app with debug mode on
