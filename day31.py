import csv
import datetime

def save_transactions(transactions, filename="transactions.csv"):
    try:
        with open(filename, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
            for t in transactions:
                writer.writerow([t["date"], t["category"], t["description"], t["amount"]])
        print("Transactions saved successfully")
    except IOError:
        print("Error: Could not save transactions. Check permissions or path.")

def load_transactions(filename="transactions.csv"):
    transactions = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append({
                    "date": row["Date"],
                    "category": row["Category"],
                    "description": row["Description"],
                    "amount": float(row["Amount"])
                })
    except(FileNotFoundError, KeyError, ValueError):
        return []
    return transactions

def add_transaction(transactions, category, description, amount):
    if not isinstance(category, str) or not category:
        print("Error: Category must be a non-empty string (e.g, Income, Expense)")
        return
    if not isinstance(description, str) or not description:
        print("Error: Descriptions must be a non-empty string.")
        return
    if not isinstance(amount, (int, float)) or amount == 0:
        print("Error: Amount must be a a non-zero number(positive for income and negative for expenses)")
        return
    transaction = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "category": category.capitalize(),
        "description": description,
        "amount": float(amount)
    }
    transactions.append(transaction)
    print(f"Added tranaction: {category} - {description} ({amount})")

def view_transactions(transactions):
    if transactions:
        print("Finance Tracker: ")
        for i, t in enumerate(transactions, 1):
            print(f"{i}. {t['date']} - {t['category']}: {t['description']} ({t['amount']})")
    else:
        print("No transactions yet! Start tracking your finances!")

def summarize_transactions(transactions):
    if not transactions:
        print("No transactions to summarise!")
        return
    summary = {}
    for t in transactions:
        summary[t["category"]] = summary.get(t["category"], 0) + t["amount"]
    print("Financial Summary by Category: ")
    for category, total in sorted(summary.items()):
        print(f"{category}: {total}")
    print(f"Net balance: {sum(t['amount'] for t in transactions)}")

name = input("Please enter your name: ")
print(f"Hey {name}, let's begin tracking your finances like a pro!")
transactions = load_transactions()
view_transactions(transactions)

while True:
    print("\nOptions: 'add to add a transaction, 'view' to see transactions, 'summarize' to see totals, 'save' to save or 'quit' to exit.")
    action = input("Choose your action: ").lower()

    if action == 'quit':
        save_transactions(transactions)
        print(f"Goodbye {name} Your finances are saved!")
        view_transactions(transactions)
        break
    elif action == 'view':
        view_transactions(transactions)
    elif action == 'summarize':
        summarize_transactions(transactions)
    elif action == 'save':
        save_transactions(transactions)
    elif action == 'add':
        category = input("Enter category(e.g., Income, Expense): ")
        description = input("Enter description(e.g., Salary, Rent): ")
        try:
            amount = float(input("Please enter the amount(positive for income and negative for an expense): "))
            add_transaction(transactions, category, description, amount)
        except ValueError:
            print("Error: Amount must be a number!")
    else:
        print("Error: Please enter 'add', 'view', 'summarise', 'save' or 'quit'")
        continue

    if transactions:
        print(f"Great job, {name}! You're managing finances like a Wall Street pro!")




