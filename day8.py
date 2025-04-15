number = int(input("Enter a number: "))
if number > 0:
    if number % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Not Positive")

while True:
    try:
        age_input = input("Enter your age (or 'q' to quit): ")
        if age_input.lower() == 'q':
            print("Goodbye!")
            break
        age = int(age_input)

        if age >= 0 :
            if age <= 3:
                print("Category: Toddler")
            elif age <= 12:
                print("Category: Child")
            elif age <= 19:
                    print("Category: Teen")
            elif age <= 59:
                        print("Category: Adult")
            else:
                        print("Category: Senior")
        else:
            print("Invalid age! Age cannot be negative.")
    except ValueError:
        print("Enter a valid number or 'q' to quit.")
