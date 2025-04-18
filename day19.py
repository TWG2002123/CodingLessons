name  = input("Please enter your name: ")
print(f"Hey {name}, Let's track your score")

score  = 0

def add_point(points = 1):
    global score
    try:
        score += points
        print(f"Hey {name}, You got a point! Your new score is {score}")
    except TypeError:
        print("Invalid input! Please enter a valid number")

def reset_score():
    global score
    score = 0
    print("Score reset to 0")

while True:
    action = input("Enter 'add' to add points, 'reset' to reset the score or 'quit': ").lower()
    if action == "quit":
        print(f"Thanks {name}! Your final score is {score}")
    elif action == "reset":
        reset_score()
    elif action == "add":
        while True:
            try:
                points = int(input("Please enter a number between 1 and 5: "))
                if points < 1 or points > 5:
                    print("Please enter a number between 1 and 5")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number")
        add_point(points)
    else:
        print("Invalid input! Please enter either 'add', 'reset' or 'quit'")

