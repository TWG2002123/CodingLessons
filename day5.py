# Get user input from lesson 3

name = input("enter your name:")

# Print number and squares with conditions (lessons 2 and 4)

print("Hey", name,  "Here are number 1-10 and their squares:")

for i in range(1,6):
    square = i * i
    if square % 2 ==0:
        status = "even"
    else:
        status = "odd"
    print(i, "squared is", square, "(" + status + ")")
