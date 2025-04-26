# Student Grades Tracker
grades = {}

def add_student(student, grade):
    if not isinstance(student, str):
        print("Error: Student name must be a string.")
        return
    if not isinstance(grade, int) or grade < 0 or grade > 100:
        print("Error: Grade must be an integer between 0 and 100.")
        return
    if student in grades:
        print(f"Error: {student} already exists. Use 'update' to change grade.")
        return
    grades[student] = grade
    print(f"Added {student}: {grade}")

def update_students(updates):
    invalid = [(s, g) for s, g in updates.items() if not isinstance(s, str) or not isinstance(g, int) or g < 0 or g > 100]
    if invalid:
        print(f"Error: Invalid updates for {', '.join(s for s, _ in invalid)}. Student names must be strings and grades must be integers between 0 and 100.")
        return
    non_existent = [s for s in updates if s not in grades]
    if non_existent:
        print(f"Error: Students {', '.join(non_existent)} not found. Use 'add' to add new students.")
        return
    grades.update(updates)
    print(f"Updated grades for {', '.join(updates.keys())}")

def remove_student(student):   
    if not isinstance(student, str):
        print("Error: Student name must be a string.")
        return
    grade = grades.pop(student, None)
    if grade is None:
        print(f"Error: {student} not found.")
    else:
        print(f"{student} has been successfully removed.")

def view_grades():
    if grades:
        print("Student Grades:")
        for student, grade in sorted(grades.items()):
            print(f"- {student}: {grade}")
    else:
        print("No students added yet. Let's get started!")

name = input("Please enter your name: ")
print(f"Hey {name}, let's do some grade sorting with a Liverpool FC spirit!")
view_grades()

while True:
    print("\nOptions: 'add' to add a student, 'update' to update a student's grade, 'remove' to remove a student, 'view' to see grades, 'quit' to exit")
    action = input("Choose an action: ").lower()
    if action == 'quit':
        print(f"Goodbye {name}! Your students and their grades:")
        view_grades()
        break
    elif action == 'view':
        view_grades()
    elif action == 'remove':
        student = input("Please enter the name of the student to remove: ")
        remove_student(student)
    elif action == 'add':
        student = input("Please enter the name of the student to add: ")
        try:
            grade = int(input("Please enter a grade (0-100): "))
            add_student(student, grade)
        except ValueError:
            print("Error: Grade must be an integer.")
    elif action == 'update':
        updates = {}
        print("Enter student-grade pairs (e.g., Alice 85, enter 'done' to finish):")
        while True:
            student = input("Student name (or 'done'): ").lower()
            if student == "done":
                break
            try:
                grade = int(input(f"Grade for {student} (0-100): "))
                updates[student] = grade
            except ValueError:
                print("Error: Grade must be an integer.")
        if updates:
            update_students(updates)
    else:
        print("Error: Please enter 'add', 'update', 'remove', 'view', or 'quit'.")
        continue

    # Theme reinforcement
    if grades:
        print(f"Great job, {name}! You're coaching students like an Anfield star!")
