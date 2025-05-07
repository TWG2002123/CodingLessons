# Interactive task app with file error handling and CRUD

import json
import datetime
import os  # Used for file operations, seen in Lesson 29 for path handling

def save_tasks(tasks, filename="tasks.json"):
    try:
        # Write tasks to JSON file with pretty-printing
        # NEW indent=2 formasts JSON with 2-space indentation for readability
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=2)
        print("Tasks saved successfully!")
    except PermissionError:
        print(f"Error: No permission to write to {filename}. Check file permissions.")
    except IOError as e:
        # NEW: 'as e' captures the IOError object, str(e) gets its error message
        print(f"Error: Could not write to {filename}. {str(e)}")
    except TypeError:
        # NEW: TypeError handles invalid data (e.g., non-serializable objects)
        print("Error: Invalid format for saving tasks.")

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Note: {filename} not found. Starting with an empty task list.")
        return []
    except json.JSONDecodeError:
        #NEW: json.JSONDecodeError handles corrupted or invalid JSON files.
        print(f"Error: {filename} is corrupted or invalid JSON.")
        return []
    except PermissionError:
        print(f"Error: No permission to read {filename}")
    except IOError as e:
        print(f"Error: Could not write to {filename}. {str(e)}")
        return []

def add_task(tasks, task, date):
    #NEW: .strip() removes leading / trailing whitespace, ensures non-empty input
    if not isinstance(task, str) or not task.strip():
        print("Error: Task must be a non-empty string.")
        return
    if not isinstance(date, str) or not date.strip():
        print("Error: Date must be a non-empty string (e.g., 2025-05-15).")
        return
    tasks.append({
        "task": task,
        "date": date,
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
        print("Liverpool FC Tasks List: ")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t['task']} (due: {t['date']}, Created: {t['created']})")
    else:
        print("No tasks yet! Plan some Anfield Events.")

name = input("Please enter your name: ")
print(f"Hey {name}, Let's manage your LFC tasks like a pro!")
tasks = load_tasks()
view_tasks(tasks)

while True:
    print("\nOptions: 'add' to add a task, 'delete' to delete a task, 'view' to see tasks, 'save' to save 'quit' to exit")
    action = input("Choose an action: ").lower()

    if action == 'quit':
        save_tasks(tasks)
        print(f"Goodbye {name}. Here is your final tasks list!")
        view_tasks(tasks)
        break
    elif action == 'view':
        view_tasks(tasks)
    elif action == 'save':
        save_tasks(tasks)
    elif action == 'add':
        task = input("Enter Task (e.g., Buy a Season Ticket): ")
        date = input("Enter due date (e.g., 2025-05-14): ")
        add_task(tasks, task, date)
    elif action == 'delete':
        view_tasks(tasks)
        try:
            index = int(input("Please enter the number of the task you want to delete (1-based): ")) - 1
            delete_task(tasks, index)
        except ValueError:
            print("Error: Please enter a valid integer.")
    else:
        print("Please enter either 'add', 'delete', 'view', 'save' or 'quit'.")
        continue

    if tasks:
        print(f"Great job, {name}! You're planning Anfield like a champion!")
        

