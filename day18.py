def divide (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ("Error! Please enter a number other than 0")
    
num = float(input("Please enter your numerator: "))
denom = float(input("Please enter your denominator: "))
result = divide(num, denom)
print(f"Hey There! {num} divided by {denom} = {result}")  

name =  input("Please enter your name: ")

def divide (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ("Error. Please enter a number that is not zero!")
    except TypeError:
        return ("Error. Please enter a valid input")
    
while True:

    while True:
        try:
            num = float(input("Please enter your numerator (or '0' to quit) "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number")

    if num == 0:
        print(f"Goodbye {name}!")
        break

    while True:
        try:
            denom = float(input("Please enter your denominator: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number")

    result = divide (num, denom)
    print (f"Hey {name}! {num} / {denom} = {result}")

      
