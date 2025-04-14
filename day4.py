# Get user input
name = (input("Enter your name:"))
num = float(input("enter a number," + name + ":"))

# Check if number is positive, negative or zero

if num > 0:
    message = "Wow, " + name + "," + str(num) + "is positive!"
elif num < 0:
    message = "Wow, " + name + "," + str(num) + "is negative!"
else:
    message = "Wow, " + name + "," + str(num) + "is zero!"

print(message)
print("Number's absolute value", abs(num))
