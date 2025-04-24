# Basic dictionary manager

player_stats = {"Salah": 23, "Nunez": 10}

def add_player(player, goals):
    if not isinstance(player, str):
        print("Error! Player name must be a string! Please try again.")
        return
    if not isinstance(goals, int) or goals < 0:
        print("Error! Goals must be an integer and cannot be negative. Please try again.")
        return
    if player in player_stats:
        print(f"Error: {player} already exists. Use 'update' to change goals.")
        return
    player_stats[player] = goals
    print(f"You added {player}: {goals}.")

def update_player(player, goals):
    if player not in player_stats:
        print("Error! This player does not exist...please try again.")
        return
    if not isinstance(goals, int) or goals < 0:
        print("Error! Goals must be an integer and cannot be negative. Please try again.")
        return
    player_stats[player] = goals
    print(f"Updated. {player}; {goals} goals.")

def remove_player(player):
    if player not in player_stats:
        print("Error! This player does not exist...please try again.")
        return
    goals = player_stats.pop(player)
    print(f"Removed {player}: {goals} goals.")

def view_stats():
    if player_stats:
        print("Here are your LFC player stats: ")
        for player, goals in sorted(player_stats.items()):
            print(f"- {player}: {goals} goals")
    else:
        print("No players yet! Add some Anfield stars to get started!")

name = input("Please enter your name: ")
print(f"Hey {name}, let's get started on those Anfield stats.")

while True:

    print("\nPlease see the following options: 'add' to add a player, 'remove' to remove a player, 'update' to update a player's stats, 'view' to view LFC player stats or 'quit'.")
    action = input("Please enter one of the aforementioned options: ").lower()
    if action == 'quit':
        print(f"Goodbye {name}! You managed {len(player_stats)} for LFC.")
        view_stats()
        break
    elif action == 'view':
        view_stats()
    elif action == 'remove':
        player = input("Please enter the player you would like to remove: ")
        remove_player(player)
    elif action == 'add':
        player = input("Please enter the name of the player you would like to add: ")
        try:
            goals = int(input("Please enter the number of goals they have scored: "))
            add_player(player, goals)
        except ValueError:
            print("Error! Please enter a string for the player name and an integer for the goals.")
    elif action == 'update':
        player = input("Please enter the name of the player you would like to update: ")
        try:
            goals = int(input("Please enter the updated number of goals: "))
            update_player(player, goals)
        except ValueError:
            print("Error! Please enter a string for the player name and an integer for the goals.")
    else:
        print("Error! Please enter either 'add', 'remove', 'view', 'update' or 'quit'. ")
        continue



