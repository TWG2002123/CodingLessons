def get_squares(start, end):
    if not isinstance (start, int) or not isinstance(end, int):
        return "Invalid! Input must me integers."
    if start > end or start < 1:
        return "Invalid! Start must be equal to or less than end AND equal to or greater than 1"
    return [x * x for x in range(start, end + 1)]

def get_even_squares(start, end):
    if not isinstance (start, int) or not isinstance(end, int):
        return "Invalid! Input must me integers."
    if start > end or start < 1:
        return "Invalid! Start must be equal to or less than end AND equal to or greater than 1"
    return [x * x for x in range(start, end + 1) if x % 2 == 0]

name = input("Please enter your name: ")
print(f"Hey {name}, let's work on some squares lists! ")

while True:
    print("n\Options: 'all' for squares, 'even' for even squares or 'quit'")
    action = input("Choose an action: ").lower()
    
    if action == 'quit':
        print(f"Goodbye {name}!")
        break
    elif action in ["all", "even"]:
        while True:
            try:
                start = int(input("Enter start number (1 or more): "))
                end = int(input("Enter end number: "))
                if start < 1 or end < start:
                    print("Invalid range! Start must be >= 1 and <= end.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter numbers.")

        if action == "all":
            result = get_squares(start, end)
        else:  # action == "even"
            result = get_even_squares(start, end)

        if isinstance(result, str):  # Error message
            print(result)
        else:
            print(f"Squares from {start} to {end}: {result}")
    else:
        print("Invalid action! Try 'all', 'even', or 'quit'.")


