# To-do list app with robust text file loading
import csv
import datetime
import os

def save_tasks(tasks, filename="data/tasks.txt"):
    try:
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["title", "due_date", "status", "created", "priority"])
            for task in tasks:
                writer.writerow([
                    task["title"],
                    task["due_date"],
                    task["status"],
                    task["created"],
                    task.get("priority", "")
                ])
        print("Tasks saved successfully!")
        return True
    except PermissionError:
        print(f"Error: No permission to write to {os.path.abspath(filename)}.")
        return False
    except IOError as e:
        print(f"Error: Could not write to {os.path.abspath(filename)}. {str(e)}")
        return False
    except TypeError:
        print("Error: Invalid data format for saving tasks.")
        return False

def load_tasks(filename="data/tasks.txt"):
    # New: Robust CSV Parsing with error recovery and data validation
    tasks = []
    skipped_rows = []
    try:
        if not os.path.exists(filename):
            print(f"Note: {filename} not found. Starting with an empty task list.")
            return []
        with open (filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            required_fields = ["title", "due_date", "status", "created"]
            valid_statuses = {"pending", "completed"}
            for row_num, row in enumerate(reader, start=2): # Start at 2 (after header)
                try:
                    # NEW: Data validation during loading
                    if not all(field in row for field in required_fields):
                        skipped_rows.append((row_num, "Missing required fields"))
                        continue
                    if not row["title"]:
                        skipped_rows.append((row_num, "Empty title"))
                        continue
                    if not row["due_date"]:
                        skipped_rows.append((row_num, "Empty due_date"))
                        continue
                    try:
                        datetime.datetime.strptime(row["due_date"], "%Y-%m-%d")
                    except ValueError:
                        skipped_rows.append((row_num, f"Invalid due_date format: {row['due_date']}"))
                        continue
                    if row ["status"] not in valid_statuses:
                        skipped_rows.append((row_num, f"Invalid status: {row['status']}"))
                        continue
                    if not row["created"]:
                        skipped_rows.append((row_num, "Empty created timestamp"))
                        continue
                    task = {
                        "title": row["title"],
                        "due_date": row["due_date"],
                        "status": row["status"],
                        "created": row["created"]
                    }
                    if row.get("priority"): # Handle optional priority field
                        task["priority"] = row["priority"]
                    task.append(task)
                except Exception as e:
                    skipped_rows.append((row_num, f"Parsing error: {str(e)}"))
                    continue
        # NEW: Logging skipped rows
        if skipped_rows:
            print(f"Warning: Skipped {len(skipped_rows)} invalid rows in {filename}:")
            for row_num, reason in skipped_rows:
                print(f" Row {row_num}: {reason}")
        return tasks
    except FileNotFoundError:
        print(f"Note: {filename} not found. Starting with an empty task list.")
        return []
    except csv.Error:
        print(f"Error: {os.path.abspath(filename)} is corrupted or invalid CSV.")
        return []
    except PermissionError:
        print(f"Error: No permission to read {os.path.abspath(filename)}.")
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
    if index is None and title is None:
        print("Error: Must provide index or title to delete.")
        return
    if index is not None:
        if not isinstance(index, int) or index < 0 or index >= len(tasks):
            print("Error: Invalid index.")
            return
        task = tasks.pop(index)
        print(f"Deleted task: {task['title']} (Due: {task['due_date']})")
    else:
        title = title.lower().strip()
        for i, task in enumerate(tasks):
            if task["title"].lower() == title:
                task = tasks.pop(i)
                print(f"Deleted task: {task['title']} (Due: {task['due_date']})")
                return
        print(f"Error: No task found with title '{title}'.")

def quit_app(tasks):
    saved = save_tasks(tasks)
    print(f"Goodbye, {name}! Your Anfield tasks {'are saved' if saved else 'could not be saved due to an error'}.")
    view_tasks(tasks)
    return True

def main_menu(tasks):
    menu_options = {
        "1": {"label": "Add Task", "action": lambda: add_task(
            tasks,
            input("Enter task title (e.g., Plan Anfield Event): "),
            input("Enter due date (YYYY-MM-DD, e.g., 2025-05-20): "),
            input("Enter status (pending, completed): "),
            input("Enter priority (high, medium, low, or leave blank): ")
        )},
        "2": {"label": "View Tasks", "action": lambda: view_tasks(tasks)},
        "3": {"label": "Delete Task", "action": lambda: (
            view_tasks(tasks),
            delete_task(tasks, index=int(input("Enter task number to delete (1-based): ")) - 1)
            if input("Delete by (1) index or (2) title? Enter 1 or 2: ").strip() == "1"
            else delete_task(tasks, title=input("Enter task title to delete: "))
        )},
        "4": {"label": "Save Tasks", "action": lambda: save_tasks(tasks)},
        "5": {"label": "Quit", "action": lambda: quit_app(tasks)}
    }
    valid_options = list(menu_options.keys())
    while True:
        print("\nLiverpool FC To-Do List Menu:")
        for key, option in menu_options.items():
            print(f"{key}: {option['label']}")
        choice = input(f"Choose an option ({min(valid_options)}-{max(valid_options)}): ").strip()
        if choice not in valid_options:
            print(f"Error: Please enter a number from {min(valid_options)} to {max(valid_options)}.")
            continue
        try:
            if menu_options[choice]["action"]():
                break
        except ValueError:
            print("Error: Invalid input for the selected action.")
            continue
        except IndexError:
            print("Error: Invalid task index.")
            continue
        if tasks:
            print(f"Great job, {name}! You're planning Anfield like a champion!")

name = input("Please enter your name: ")
print(f"Hey {name}, let's manage Liverpool FC tasks like a pro!")
tasks = load_tasks()
main_menu(tasks)
