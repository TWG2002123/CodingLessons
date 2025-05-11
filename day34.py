# Mini-project: Note-taking app combining files, lists, and error handling
import json
import datetime
import os

def save_notes(notes, filename="notes.json"):
    try:
        # NEW: Create directory if it doesn't exist using os.makedirs
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        with open(filename, "w") as file:
            json.dump(notes, file, indent=2)
        print("Notes saved successfully!")
    except PermissionError:
        print(f"Error: No permission to write to {os.path.abspath(filename)}.")
    except IOError as e:
        print(f"Error: Could not write to {os.path.abspath(filename)}. {str(e)}")
    except TypeError:
        print("Error: Invalid datea format for saving notes.")

def load_notes(filename="notes.json"):
    try:
        if not os.path.exists(filename):
            print(f"Note: {filename} not found. Starting with an empty note list.")
            return []
        with open(filename, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {os.path.abspath(filename)} is corrupted or invalid JSON.")
        return []
    except PermissionError:
        print(f"Error: No permision to read {os.path.abspath(filename)}.")
        return []
    except IOError as e:
        print(f"Error: Could not read {os.path.abspath(filename)}. {str(e)}")
        return []

def add_note(notes, title, content, category):
    title = title.strip()
    content = content.strip()
    category = category.lower().strip()
    if not title or not isinstance (title, str):
        print("Error: Title must be a non-empty string.")
        return
    if not content or not isinstance (content, str):
        print("Error: Content must be a non-empty string.")
        return
    if not category or not isinstance (category, str):
        print("Error: Category must be a non-empty string (e.g., plannaing, logistics).")
        return
    note = {
        "title": title,
        "content": content,
        "category": category,
        "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
     # NEW: Use json.dumps to log the note as a formatted string for confirmation
    print(f"Added note:\n{json.dumps(note,indent=2)}")

def update_note(notes, index, title, content, category):
    if not isinstance(index, int) or index < 0 or index >= len(notes):
        print("Error: Invalid note index.")
        return
    title = title.strip()
    content = content.strip()
    category = category.strip()
    if not title or not isinstance (title, str):
        print("Error: Title must be a non-empty string.")
        return
    if not content or not isinstance (content, str):
        print("Error: Content must be a non-empty string.")
        return
    if not category or not isinstance (category, str):
        print("Error: Category must be a non-empty string.")
        return
    notes[index] = {
        "title": title,
        "content": content,
        "category": category,
        "created": notes[index]["created"], # Preserve original timestamp
        "updated": datetime.datetime.now.strftime("%Y-%m-%d %H:%M:%S")
    }
    print(f"Updated note: {title}")

def delete_note(notes, index):
    if not isinstance(index, int) or index < 0 or index >= len(notes):
        print("Error: Invalid note index")
        return
    note = notes.pop(index)
    print(f"Deleted note: {note['title']}")

def view_notes(notes):
    if notes:
        print("Liverpool FC Note-Taking App:")
        # NEW: enumerate(start=1) uses 1-based indexing for user-friendly display
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note['title']} (Category: {note['category']}, Created: {note['created']})")
            print(f"     Content: {note['content']}")
            if "updated" in note:
                print(f"    Updated: {note['updated']}")
    else:
        print("No notes yet! Start jotting down Anfield plans!")

name = input("Please enter your name: ")
print(f"Hey {name}, let's manage Liverpool FC notes like a pro!")
notes = load_notes()

while True:
    print("\nOptions: 'add', 'update, 'delete', 'view', 'save' or 'quit'")
    action = input("Choose an action: ").lower().strip()
    if not action:
        print("Error: Action cannot be empty.")
        continue

    if action == 'quit':
        save_notes(notes)
        print(f"Goodbye {name}, here are your final notes: ")
        view_notes(notes)
        break
    elif action == 'view':
        view_notes(notes)
    elif action == 'save':
        save_notes(notes)
    elif action == 'add':
        title = input("Enter note title(e.g., Plan Anfield Event): ")
        content = input("Enter note content: (e.g., Book flights for match): ")
        category = input("Enter category (e.g., planning, logistics): ")
        add_note(notes, title, content, category)
    elif action == 'update':
        view_notes(notes)
        try:
            index = int(input("Enter note number to update (1-based): ")) - 1
            title = input("Enter new title (or press Enter to keep unchanaged): ")
            content = input("Enter new content (or press Enter to keep unchanged): ")
            category = input("Enter new category (or press Enter to keep unchanged): ")
            update_note(notes, index, title or notes[index]["category"])
        except ValueError:
            print("Error: Note number must be an integer.")
    elif action == 'delete':
        view_notes(notes)
        try:
            index = int(input("Enter note number to delete (1-based): ")) - 1
            delete_note(notes, index)
        except ValueError:
            print("Error: Note number must be an integer.")
    else:
        print("Error: Please enter 'add', 'update', 'delete', 'view', 'save' or 'quit.")
        continue

    if notes:
        print(f"Great job, {name}! You're organizing Anfield like a champion!")
