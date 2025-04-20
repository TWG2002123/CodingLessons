tasks = []

def get_first_last(tasks):
    if tasks:
        first = tasks[0]
        last = tasks[-1]
        return f"first task is: {first} last task: {last}"
    return "no tasks available."

def add_task(task):
    if task.strip() == "":
        return "Task cannot be empty. Please try again."
    tasks.append(task)
    return

def view_tasks():
    if tasks:
        print("Your tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

name = input("Please enter your name: ")
print(f"Hey {name}, Let's take a look at your tasks")

while True:

    print("\nPlease enter one of the following: 'add', 'get first/last', 'view' or 'quit'")
    action = input("Choose an action: ").lower()
    if action == 'quit':
        print(f"Goodbye {name}!")
        view_tasks()
        break
    elif action == 'add':
        task = input("Please enter the task you would like to add: ")
        add_task(task)
        print(f"You added {task} to your list.")
    elif action == 'view':
        view_tasks()
    elif action == 'get first/last':
        print(get_first_last(tasks))
    else:
        print("Invalid input please try again.")
        

    
    

