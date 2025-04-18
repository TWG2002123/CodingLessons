# Calculating area using two parameters inside a function

name = input("Please enter your name: ")
print(f"Nice to meet you {name}. Let's calculate some areas together!")

def area(length, width):
    return length * width

while True:
    
    while True:
        try:
            length = float(input("Please enter the length of the rectangle (or '0' to quit): "))
            if length < 0:
                print("Please enter a positive number")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a positive number")
    if length == 0:
        print(f"Thank you for playing {name}. Goodybye!")
        break
    while True:
        try:
            width = float(input("Please enter the width of the rectangle (or '0' to quit): "))
            if width < 0:
                print("Please enter a positive number")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a positive number")
    if width == 0:
        print(f"Thank you for playing {name}. Goodbye!")
        break
        
    result = area(length, width)
    print(f"The area of a {length} x {width} rectangle is {result}")
