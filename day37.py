import json
import datetime
import os

def save_tasks(tasks, filename="data/tasks.json"):
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=2)
        print("Tasks saved successfully!")
    except PermissionError:
        print(f"Error: No permission to write to {os.path.abspath(filename)}.")
    except IOError as e:
        print(f"Error: Could not write to {os.path.abspath(filename)}. {str(e)}")
    except TypeError:
        print("Error: Invalidn data format for saving tasks.")

def load_tasks(filename="data/taks.json"):
    try:
        if not os.path.exists(filename):
            print(f"Note: {filename} not found. Starting with an empty tasks list.")
            return []
        with open(filename, "r" ) as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {os.path.abspath(filename)} is corrupted or invalid JSON.")
        return []
    except PermissionError:
        print(f"Error: No permission to read {os.path.abspath(filename)}.")
        return []
    except IOError as e:
        print(f"Error: Could not read {os.path.abspath(filename)}. {str(e)}.")
        return []
    
def add_task(tasks, title, due_date, status):
    # NEW: Input validation with custom constraints for status
    title = title.strip()
    due_date = due_date.strip()
    status.lower().strip()
    if not isinstance(title, str) or not title:
        print("Error: Title must be a non-empty string.")
        return
    if not isinstance(due_date, str) or not due_date:
        print("Error: Due date must be a non-empty string (e.g., 2025-05-25).")
        return
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Due date must be in the YYYY-MM-DD format (e.g., 2025-06-23).")
        return
    valid_statuses = ["pending", "completed"]
    if not isinstance(status, str) or status not in valid_statuses:
        print(f"Error: Status must be one of {valid_statuses}.")
        return
     # NEW: Dictionary initialization with default values (status, created timestamp)
    task = {
         "title": title,
         "due_date": due_date,
         "status": status,
         "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")# NEW: Timestamp as default field
    }
    tasks.append(task)
    print(f"Added task: {title} (Due: {due_date}, Status: {status})")

# Placeholder for viewing tasks (to be implemented in future lessons)
def view_tasks(tasks):
    print("View tasks: Not yet implemented.")

# Placeholder for deleting tasks
def delete_task(tasks, index):
    print("Delete task: Not yet implemented.")

name = input("Please enter your name: ")
print(f"Hey {name}, let's manage your LFC tasks like a pro!")
tasks = load_tasks()

while True:
    print("\nOptions: 'add', 'view', 'delete', 'save', 'quit'")
    action = input("Choose an action: ").lower().strip()
    if not action:
        print("Error: Action can not be empty.")
        continue

    if action == 'quit':
        save_tasks(tasks)
        print(f"Goodbye, {name}! your tasks are saved.")
        view_tasks(tasks)
        break
    elif action == 'view':
        view_tasks(tasks)
    elif action == 'save':
        save_tasks(tasks)
    elif action == 'add':
        title = input("Enter task title (e.g., Plan Anfield Event): ")
        due_date = input("Enter due date (YYYY-MM-DD):  ")
        status = input("Enter 'pending' or 'completed: ")
        add_task(tasks, title, due_date, status)
    elif action == 'delete':
        view_tasks(tasks)
        try:
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        except ValueError:
            print("Error: Task number must be an integer.")
    else:
        print("Error: Please enter 'add', 'view', 'delete', 'save', or 'quit'.")

    if tasks:
        print(f"Great job, {name}! You're planning Anfield tasks like a pro.")
