#Basic Trade CSV Logger

import csv
import datetime

def save_trade(trades, filename="trades.csv"):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Pair", "Action", "Price", "Volume"])
            for trade in trades:
                writer.writerow([trade["date"], trade["pair"], trade["action"], trade["price"], trade["volume"]])
        print("Trades saved successfully!")
    except IOError:
        print("Error: Could not save trade to file.")

def load_trades(filename = "traders.csv"):
    trades = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                trades.append({
                    "date": row["Date"],
                    "pair": row["Pair"],
                    "action": row["Action"],
                    "price": float(row["Price"]),
                    "volume": int(row["Volume"])
                })
    except (FileNotFoundError, ValueError, KeyError):
        return []
    return trades

def add_trade(trades, pair, action, price, volume):
    if not isinstance(pair, str) or not pair:
        print("Error: Pair must be a non-empty string (e.g GBP/USD).")
        return
    if action not in ["Buy", "Sell"]:
        print("Error: Action must be 'Buy' or 'Sell'.")
        return
    if not isinstance(price, float) or price <= 0:
        print("Error: Price must be a positive number.")
        return
    if not isinstance(volume, int) or volume <= 0:
        print("Error: Volume must be a positive integer.")
        return
    trade = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pair": pair,
        "action": action,
        "price": price,
        "volume": volume
    }
    trades.append(trade)
    print(f"Added Trade: {action} {volume} {pair} at {price}")

def view_trades(trades):
    if trades:
        print("Here is your trade log: ")
        for i, trade in enumerate(trades, 1):
            print(f"{i}. {trade['date']} - {trade['action']} {trade['volume']} {trade['pair']} at {trade['price']}")
    else:
        print("No trades yet! Start logging some forex action!")

name = input("Please enter your name: ")
print(f"Hey {name}, Let's start logging your forex trades together.")
trades = load_trades()
view_trades(trades)

while True:
    print("\nOptions: 'add' to add a trade, 'view' to view trades, 'save' to save file or 'quit'")
    action = input("Please enter your action: ").lower()

    if action == 'quit':
        save_trade(trades)
        print(f"Goodbye {name}! Please see your final trades here: ")
        view_trades(trades)
        break
    elif action == 'view':
        view_trades(trades)
    elif action == 'save':
        save_trade(trades)
    elif action == 'add':
        pair = input("Please enter your currency pair (e.g EUR/USD): ").upper()
        action = input("Please enter either 'Buy' or 'Sell': ").capitalize()
        try:
            price = float(input("Please enter the price (e.g 1.247282): "))
            volume = int(input("Please enter the volume (e.g 1000): "))
            add_trade(trades, pair, action, price, volume)
        except ValueError:
            print("Error: Price must be a number and volume must be an integer.")
    else:
        print("Error: Please enter 'add', 'view', 'save', or 'quit'.")
        continue








