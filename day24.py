#basic tic-tac-toe board

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def display_board():
    print(" 1 2 3")
    for i, row in enumerate(board, 1):
        print(f"{i} {'|'.join(row)}")
        if i < 3:
            print(" -+-+-")

def place_mark(row, col, mark):
    if not isinstance(row, int) or not isinstance(col, int):
        print("Error! Please enter a valid number.")
        return False
    if not (0 <= row <= 2 and 0 <= col <= 2):
        print("Error please enter either 1, 2 or 3.")
        board[row][col] = mark
        return False
    if board[row][col] != " ":
        print("Error! Cell also taken.")
        return False
    board[row][col] = mark
    return True

def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    print("Board Reset!")


name = input("Enter your name: ")
print(f"Hey {name}, let's manage a tic-tac-toe board!")

while True:
    print("\nOptions: 'place' to add an 'X' or 'O', 'reset' to reset the board, 'view' to view the board or 'quit' to end the game")
    action = input("Please enter 'place', 'reset', 'view' or 'quit':  ").lower()
    if action == 'quit':
        print(f"Thank you for playing {name}!")
        display_board()
        break
    elif action == 'reset':
        reset_board()
    elif action == 'view':
        display_board()
    elif action == 'place':
        while True:
            try:
                row = int(input("Please enter a number between 1 and 3 for your row: ")) - 1
                col = int(input("Please enter a number between 1 and 3 for your column: ")) - 1
                mark = (input("Please enter either 'X' or 'O' to place your mark: ")).upper()
                if mark not in ["X", "O"]:
                    print("Error! Mark must be 'X' or 'O' please try again.")
                    continue
                if place_mark(row, col, mark):
                    break
                else:
                    print("Try again!")
            except ValueError:
                print("Error! row and column must be numbers")
        display_board()
    else:
        print("Invalid action! Try 'place', 'reset', 'view', or 'quit'.")


