import os
expenses = []
def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, description = line.strip().split(",")
                expenses.append((amount, description))
def save_expense(amount, description):
    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{description}\n")
def add_expense():
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    expenses.append((amount, description))
    save_expense(amount, description)
    print("Expense added and saved!")
def view_expenses():
    if not expenses:
        print("No expenses added yet.")
    else:
        print("\n--- All Expenses ---")
        for i, (amount, description) in enumerate(expenses, 1):
            print(f"{i}. ₹{amount} - {description}")
        print("--------------------\n")
def main():
    load_expenses()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Thankyou!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
