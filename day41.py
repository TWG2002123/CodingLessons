import json
import os

def add_task(tasks, task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else " "
        print(f"{i}. [{status}] {task['name']}")

def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Task '{tasks[task_index - 1]['name']}' marked as complete.")
    else:
        print("Invalid task number.")

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)
    print("Tasks saved.")

def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Save and Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            add_task(tasks, task_name)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                task_index = int(input("Enter task number to mark complete: "))
                complete_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
