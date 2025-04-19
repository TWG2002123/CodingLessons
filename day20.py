tasks = []

while True:
    def add_task(task):
        if task.strip() == "":
            print("Error. Task cannot be empty.")
        else:
            tasks.append(task)
            print(f"You added '{task}' to your list.")
    
    def remove_task(index):
        try:
            task = tasks.pop(index - 1)
            print(f"You removed '{task}' from your list")
        except IndexError:
            print("Error, Please enter a valid task number to remove")
        except ValueError:
            print("Please enter a valid number.")

    def view_tasks():
        if tasks:
            print("Your tasks are: ")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks present.")

    name = input("Please enter your name: ")
    print(f"Hey {name}! Let's get started on your to-do list.")

    while True: 
        action = input("Please enter one of the following: 'add', 'remove', 'view' or 'quit': ").lower()
        if action == "quit":
            print(f"Goodbye {name}")
            view_tasks()
            break
        elif action == "add":
            task = input("Please enter your task:")
            add_task(task)
        elif action == "remove":
            view_tasks()
            index = input("Please enter the number of the task you would like to remove (or 'cancel'): ")
            if index.lower() != 'cancel':
                try:
                    remove_task(int(index))
                except ValueError:
                    print("Please enter a valid number.")
        elif action == "view":
            view_tasks()
        else:
            print("Invalid input. Please enter either 'add', 'remove', 'view' or 'quit'")
            

            
 

                
