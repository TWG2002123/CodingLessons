# Inventory Manager
inventory = {}

def add_item(item, quantity):
    if not isinstance(item, str):
        print("Error: Item name must be a string.")
        return
    if not isinstance(quantity, int) or quantity < 0:
        print("Error: Quantity must be a non-negative integer.")
        return
    if item in inventory:
        print(f"Added {quantity} to existing {item}(s)")
    else:
        print(f"Added new {quantity} {item}(s)")
    inventory[item] = inventory.get(item, 0) + quantity

def update_item(updates):
    invalid = [(i, q) for i, q in updates.items() if not isinstance(i, str) or not isinstance(q, int) or q < 0]
    if invalid:
        print(f"Error: Invalid updates for {', '.join(i for i, _ in invalid)}. Items must be strings and quantities must be non-negative integers.")
        return
    inventory.update(updates)
    print(f"Successfully updated quantities for {', '.join(updates.keys())}")

def remove_item(item):
    if not isinstance(item, str):
        print("Error: Item name must be a string.")
        return
    quantity = inventory.pop(item, None)
    if quantity is None:
        print(f"Error: {item} not found.")
    else:
        print(f"{item}: {quantity} has been removed.")

def view_inventory():
    if inventory:
        print("Here is your LFC Inventory:")
        for item, quantity in sorted(inventory.items()):
            print(f"- {item}: {quantity} units")
    else:
        print("No inventory yet! Let's get started on building one.")

name = input("Please enter your name: ")
print(f"Hey {name}, let's get started on building your LFC inventory!")
view_inventory()

while True:
    print("\nOptions: 'add' to add an item, 'update' to update quantities, 'remove' to remove an item, 'view' to see inventory, 'quit' to exit")
    action = input("Enter your action: ").lower()
    if action == 'quit':
        print(f"Goodbye {name}! Here is your final inventory:")
        view_inventory()
        break
    elif action == 'view':
        view_inventory()
    elif action == 'remove':
        item = input("Please enter the name of the item to remove: ").lower()
        remove_item(item)
    elif action == 'add':
        item = input("Please enter the name of the item to add: ").lower()
        try:
            quantity = int(input("Please enter the number of units: "))
            add_item(item, quantity)
        except ValueError:
            print("Error: Quantity must be an integer.")
    elif action == 'update':
        updates = {}
        print("Enter item-quantity pairs (e.g., Shirt 50, enter 'done' to finish):")
        while True:
            item = input("Item name (or 'done'): ").lower()
            if item == "done":
                break
            try:
                quantity = int(input(f"Quantity for {item}: "))
                updates[item] = quantity
            except ValueError:
                print("Error: Quantity must be an integer.")
        if updates:
            update_item(updates)
    else:
        print("Error: Please enter 'add', 'update', 'remove', 'view', or 'quit'.")
        continue

    # Theme reinforcement
    if inventory:
        print(f"Great job, {name}! You're stocking Anfield like a pro!")
