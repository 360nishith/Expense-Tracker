from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
expenses = [] 

def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, description = line.strip().split(",", 1)
                expenses.append((float(amount), description))

def save_expense(amount, description):
    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{description}\n")
        
@app.route("/")
def index():
    total = sum(amount for amount, _ in expenses)
    return render_template("index.html", expenses=expenses, total=total)

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form.get("amount")
    description = request.form.get("description")
    if amount and description:
        expenses.append((float(amount), description))
        save_expense(amount, description)
    return redirect("/")

if __name__ == "__main__":
    load_expenses()
    app.run(debug=True)
