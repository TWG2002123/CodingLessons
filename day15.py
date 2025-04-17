name = input("Please enter your name: ")
print(f"Hey {name}, Let's calculate the squares of some numbers!")

def square(number):
    return number * number

while True:
    while True:
        try:
            number = int(input("Please enter a number (or '0' 'quit'): "))
            break
        except ValueError:
            print("Invalid input please enter a whole number")

    if number == 0:
        print(f"Thanks for playing {name}!")
        break
    result = square(number) 
    print(f"Hey {name}, the square of {number} is {result}")

