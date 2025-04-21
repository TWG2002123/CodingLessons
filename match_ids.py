match_ids = set()
match_details = {}

def add_match(match_id, date, opponent):
    if not isinstance(match_id, str) or not isinstance(date, str) or not isinstance(opponent, str):
        print("Error. Invalid input. All inputs here MUST be strings. Try again... ")
        return
    if match_id in match_ids:
        print(f"Error. match id: '{match_id}' already exists. Please try again. ")
        return
    match_ids.add(match_id)
    match_details[match_id] = (date, opponent)
    print(f"Added match id, {match_id}: {date}, vs {opponent}")

def remove_match(match_id):
    if not isinstance(match_id, str):
        print("Error, Match ID must be a string.")
        return
    if match_id in match_ids:
        match_ids.remove(match_id)
        print(f"match id {match_id} has been removed.")
    else:
        print(f"Match id {match_id} has not been found.")

def view_matches():
    if match_ids:
        print("Your Liverpool FC match ids: ")
        for match_id in sorted(match_ids):
            date, opponent = match_details[match_id]
            print(f"- {match_id}: {date}, {opponent}")
    else:
        print("No match id's found. Please try again.")

name = input("Enter your name: ")
print(f"Hey {name}, Let's plan some Liverpool match days.")

while True:
    print("\nOptions: 'add' to add a match, 'remove' to remove a match, 'view' to view all matches or 'quit' to exit.")
    action = input("Please select one of the actions: ").lower()
    if action == 'quit':
        print(f"Goodbye {name}! Matches managed {len(match_ids)} unique matches!")
        view_matches()
        break
    elif action == 'view':
        view_matches()
    elif action == 'add':
        match_id = input("Please Enter a unique match id (eg 'LIVCHE2025'): ")
        date = input("Please enter the date of the match (eg. '25/11/2025'): ")
        opponent = input("Please enter the opponent (eg. 'Manchester United'): ")
        add_match(match_id, date, opponent)
    elif action == 'remove':
        match_id = input("Please enter the unique match id you would like to remove: ")
        remove_match(match_id)
    else:
        print("Invalid input! Please enter 'add', 'remove', 'view' or 'quit'")

        
    


