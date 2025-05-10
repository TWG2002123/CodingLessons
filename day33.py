import json
import datetime
import os

def save_tasks(tasks, filename="tasks.json"):
    try:
        # Fixed: Corrected typo from os.paths.exists to os.path.exists
        if os.path.exists(filename):
            print(f"Overwriting existing {filename}.")
        else:
            print(f"Creating new {filename}.")
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=2)
        print("Tasks saved successfully!")
    except PermissionError:
        print(f"Error: No permission to write to {os.path.abspath(filename)}.")
    except IOError as e:
        print(f"Error: Could not write to {os.path.abspath(filename)}. {str(e)}")
    except TypeError:
        print("Error: Invalid data format for saving tasks.")

def load_tasks(filename="tasks.json"):
    try:
        if not os.path.exists(filename):
            print(f"Note: {filename} not found. Starting with an empty task list.")
            return []
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Fixed: Corrected typo from os.path.asbpath to os.path.abspath
        print(f"Error: {os.path.abspath(filename)} is corrupted or invalid JSON.")
        return []
    except PermissionError:
        print(f"Error: No permission to read {os.path.abspath(filename)}.")
        return []
    except IOError as e:
        print(f"Error: Could not read {os.path.abspath(filename)}. {str(e)}")
        return []

def add_task(tasks, task, date):
    task = task.lower().strip()
    date = date.strip()
    if not isinstance(task, str) or not task:
        print("Error: Task must be a non-empty string.")
        return
    if not isinstance(date, str) or not date:
        # Fixed: Added hyphen in "non-empty" and period after "e.g."
        print("Error: Date must be a non-empty string (e.g., 2025-05-15).")
        return
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Error: Date must be in YYYY-MM-DD format (e.g., 2025-05-15).")
        return
    tasks.append({
        "task": task,
        "date": date,
        # Fixed: Changed strptime to strftime for timestamp formatting
        "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"Added task: {task} (Due: {date})")

def delete_task(tasks, index):
    if not isinstance(index, int) or index < 0 or index >= len(tasks):
        print("Error: Invalid task index.")
        return
    task = tasks.pop(index)
    print(f"Deleted task: {task['task']} (Due: {task['date']})")

def view_tasks(tasks):
    if tasks:
        print("Liverpool FC To-Do List:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['task']} (Due: {t['date']}, Created: {t['created']})")
    else:
        print("No tasks yet! Plan some Anfield events!")

name = input("Please enter your name: ")
print(f"Hey {name}, let's manage Liverpool FC tasks like a pro!")
tasks = load_tasks()
view_tasks(tasks)

while True:
    # Fixed: Simplified prompt for clarity and usability
    print("\nOptions: 'add', 'delete', 'view', 'save', 'quit'")
    action = input("Choose an action: ").lower().strip()
    if not action:
        print("Error: Action cannot be empty.")
        continue

    if action == "quit":
        save_tasks(tasks)
        print(f"Goodbye {name}! Your Anfield tasks are saved!")
        view_tasks(tasks)
        break
    elif action == "view":
        view_tasks(tasks)
    elif action == "save":
        save_tasks(tasks)
    elif action == "add":
        task = input("Please enter the name of your task (e.g., Plan Anfield Event): ")
        date = input("Please enter the due date (e.g., 2025-06-13): ")
        add_task(tasks, task, date)
    elif action == "delete":
        view_tasks(tasks)
        try:
            index = int(input("Please enter a task number to delete (1-based): ")) - 1
            delete_task(tasks, index)
        except ValueError:
            # Fixed: Lowercased "task number" for consistency
            print("Error: Task number must be an integer.")
    else:
        # Fixed: Added comma before "or 'quit'"
        print("Error: Please enter 'add', 'delete', 'view', 'save', or 'quit'.")
        continue

    if tasks:
        print(f"Great job, {name}! You're planning Anfield like a champion!")
