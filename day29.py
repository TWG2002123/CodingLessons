tasks = []

def save_tasks(filename = "tasks.txt"):
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"{task}\n")
    except IOError:
        print("Error: Could not save tasks to file. Please check permissions and/or file path.")

def load_tasks(filename = "tasks.txt"):
    try:
        with open("tasks.txt", "r") as file:
            return[line.strip() for line in file]
    except FileNotFoundError:
        return []
    
def add_task(task):
    if not isinstance(task, str):
        print("Error. Your task must be a string. Please try again.")
        return
    if task in tasks:
        print("Error. File already exists.")
        return
    tasks.append(task)
    print(f"Added task: {task}")

def view_tasks():
    if tasks:
        print(f"Your tasks: {tasks}")
    else:
        print("No tasks. Please add a task to get started.")

name = input("Please enter your name: ")
print(f"Hey {name}, let's manage your tasks list together.")
tasks = load_tasks()
view_tasks()

while True:
    
    print("\nOptions: 'add' to add a task, 'remove' to remove a task, 'view' to view tasks, 'save' to save file or 'quit'")
    action = input("Please select your input: ").lower()

    if action == 'quit':
        save_tasks(tasks)
        print(f"Goodbye {name}! Your final tasks are: ")
        view_tasks()
        break
    elif action == 'view':
        view_tasks()
    elif action == 'save':
        save_tasks(tasks)
    elif action == 'remove':
        view_tasks()
        try:
            index = int(input("Enter a number to remove (1-based): ")) -1
            if 0 <= index < len(tasks):
                task = tasks.pop(index)
                print(f"You removed task: {task}")
            else:
                print("Error: Invalid task number.")
        except ValueError:
            print("Input must be a valid integer.")
    elif action == 'add':
        task = input("Please enter your task (e.g Buy Liverpool Season ticket for next year): ")
        add_task(task)
    else:
        print("Error: Please enter either 'add', 'remove', 'view', 'save' or 'quit'.")
