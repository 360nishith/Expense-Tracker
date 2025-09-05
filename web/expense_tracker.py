from flask import Flask, render_template, request, redirect, flash
import csv
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"

CSV_FILE = "expenses.csv"
expenses = []

def load_expenses():
    expenses.clear()
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    amount, description = row
                    expenses.append((float(amount), description))

def save_all_expenses():
    with open(CSV_FILE, mode="w", newline='') as file:
        writer = csv.writer(file)
        for amount, description in expenses:
            writer.writerow([amount, description])

def add_expense(amount, description):
    with open(CSV_FILE, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, description])
    expenses.append((float(amount), description))

@app.route("/")
def index():
    load_expenses()
    total = sum(amount for amount, _ in expenses)
    expenses_with_index = [(amount, desc, idx) for idx, (amount, desc) in enumerate(expenses)]
    return render_template("index.html", expenses=expenses_with_index, total=total)

@app.route("/add", methods=["POST"])
def add():
    amount = request.form.get("amount")
    description = request.form.get("description")
    if amount and description:
        add_expense(amount, description)
        flash("Expense added successfully!")
    return redirect("/")

@app.route("/edit/<int:idx>", methods=["GET", "POST"])
def edit(idx):
    load_expenses()
    if idx < 0 or idx >= len(expenses):
        flash("Invalid expense selected.")
        return redirect("/")

    if request.method == "POST":
        new_amount = float(request.form.get("amount"))
        new_description = request.form.get("description")
        expenses[idx] = (new_amount, new_description)
        save_all_expenses()
        flash("Expense updated successfully!")
        return redirect("/")

    amount, description = expenses[idx]
    return render_template("edit.html", amount=amount, description=description, idx=idx)

@app.route("/delete/<int:idx>")
def delete(idx):
    load_expenses()
    if idx < 0 or idx >= len(expenses):
        flash("Invalid expense selected.")
        return redirect("/")

    removed = expenses.pop(idx)
    save_all_expenses()
    flash(f"Deleted expense: ₹{removed[0]} - {removed[1]}")
    return redirect("/")

if __name__ == "__main__":
    load_expenses()
    app.run(debug=True)
