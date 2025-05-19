# To-do list app with task deletion function
import json
import datetime
import os

def save_tasks(tasks, filename="data/tasks.json"):
    try:
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=2)
        print("Tasks saved successfully!")
    except PermissionError:
        print(f"Error: No permission to write to {os.path.abspath(filename)}.")
    except IOError as e:
        print(f"Error: Could not write to {os.path.abspath(filename)}. {str(e)}")
    except TypeError:
        print("Error: Invalid data format for saving tasks.")

def load_tasks(filename="data/tasks.json"):
    try:
        if not os.path.exists(filename):
            print(f"Note: {filename} not found. Starting with an empty task list.")
            return []
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {os.path.abspath(filename)} is corrupted or invalid JSON.")
        return []
    except PermissionError:
        print(f"Error: No permission to read {os.path.abspath(filename)}.")
        return []
    except IOError as e:
        print(f"Error: Could not read {os.path.abspath(filename)}. {str(e)}")
        return []

def add_task(tasks, title, due_date, status, priority=None):
    title = title.strip()
    due_date = due_date.strip()
    status = status.lower().strip()
    if priority:
        priority = priority.lower().strip()
    if not isinstance(title, str) or not title:
        print("Error: Title must be a non-empty string.")
        return
    if not isinstance(due_date, str) or not due_date:
        print("Error: Due date must be a non-empty string (e.g., 2025-05-15).")
        return
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format (e.g., 2025-05-15).")
        return
    valid_statuses = ["pending", "completed"]
    if not isinstance(status, str) or status not in valid_statuses:
        print(f"Error: Status must be one of {valid_statuses}.")
        return
    task = {
        "title": title,
        "due_date": due_date,
        "status": status,
        "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if priority and priority in ["high", "medium", "low"]:
        task["priority"] = priority
    tasks.append(task)
    print(f"Added task: {title} (Due: {due_date}, Status: {status})")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet! Plan some Anfield events!")
        return
    print("Liverpool FC To-Do List:")
    max_title_len = max(len(task["title"]) for task in tasks)
    max_date_len = max(len(task["due_date"]) for task in tasks)
    max_status_len = max(len(task["status"]) for task in tasks)
    print(f"{'#':<3} {'Title':<{max_title_len}} {'Due Date':<{max_date_len}} {'Status':<{max_status_len}} {'Created':<20}")
    print("-" * (3 + max_title_len + max_date_len + max_status_len + 20 + 4))
    for i, task in enumerate(tasks, start=1):
        title = task["title"]
        due_date = task["due_date"]
        status = task["status"]
        created = task["created"]
        priority = task.get("priority", "")
        print(f"{i:<3} {title:<{max_title_len}} {due_date:<{max_date_len}} {status:<{max_status_len}} {created:<20}")
        if priority:
            print(f"   Priority: {priority}")

def delete_task(tasks, index=None, title=None):
    # NEW: Multiple deletion methods (index or title) in one function
    if index is None and title is None:
        print("Error: Must provide index or title to delete.")
        return
    if index is not None:
        # NEW: Index validation with bounds checking
        if not isinstance(index, int) or index < 0 or index >= len(tasks):
            print("Error: Invalid index.")
            return
        task = tasks.pop(index)
        print(f"Deleted task: {task['title']} (Due: {task['due_date']})")
    else:
        # NEW: String matching for title-based deletion
        title = title.lower().strip()
        for i, task in enumerate(tasks):
            if task['title'].lower() == task:
                task = tasks.pop(i)
                print(f"Deleted task: {task} (Due Date {task['due_date']})")
                return
        print(f"Error: No task found with the title '{title}'.")

name = input("Please enter your name: ")
print(f"Hey {name}, let's manage Liverpool FC tasks like a pro!")
tasks = load_tasks()

while True:
    print("\nOptions: 'add', 'view', 'delete', 'save', 'quit'")
    action = input("Choose an action: ").lower().strip()
    if not action:
        print("Error: Action cannot be empty.")
        continue

    if action == "quit":
        save_tasks(tasks)
        print(f"Goodbye, {name}! Your Anfield tasks are saved!")
        view_tasks(tasks)
        break
    elif action == "view":
        view_tasks(tasks)
    elif action == "save":
        save_tasks(tasks)
    elif action == "add":
        title = input("Enter task title (e.g., Plan Anfield Event): ")
        due_date = input("Enter due date (YYYY-MM-DD, e.g., 2025-05-15): ")
        status = input("Enter status (pending, completed): ")
        priority = input("Enter priority (high, medium, low, or leave blank): ")
        add_task(tasks, title, due_date, status, priority)
    elif action == "delete":
        view_tasks(tasks)
        method = input("Delete by (1) index or (2) title? Enter 1 or 2: ").strip()
        if method == "1":
            try:
                index = int(input("Enter task number to deleted (1-based): ")) - 1
                delete_task(tasks, index=index)
            except ValueError:
                print("Error: Task number must be an integer.")
        elif method == "2":
            title = input("Enter task title to delete: ")
            delete_task(tasks, title=title)
        else:
            print("Error: Please enter 1 or 2")
    else:
        print("Error: Please enter 'add', 'view', 'delete', 'save', or 'quit'.")
        continue

    if tasks:
        print(f"Great job, {name}! You're planning Anfield like a champion!")
