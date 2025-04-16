# create and manage a list
tasks = ["Learn Python", "Build App", "Test Code"]

# Access Elements

print("First Task: ", tasks[0])
print("Last Task: ", tasks[-1])

# Modify elements
tasks[1] = "Deploy App"
print("Updated List: ", tasks)

tasks.append("Debug Code")
tasks.remove("Test Code")
print("Final list of tasks: ", tasks)

# manage a list with user input
name = input("Please enter your name: ")
print(f"Hey {name}, let's manage a task list")

#create list

tasks = ["Play chess", "Go to Muay Thai", "Go to the Movies"]

# Show list with loop (Lesson 10)

print("Your tasks: ")
for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]}")

# Modify based on input
new_task = input("Add a new task: ")
tasks.append(new_task)

#Remove Task
remove_task = input ("Enter a task to remove (or 'none'): ")
if remove_task != "none" and remove_task in tasks:
    tasks.remove(remove_task)
else:
    print("no task removed. ")

# Final List
print(f"{name}'s updated tasks: ", tasks)
