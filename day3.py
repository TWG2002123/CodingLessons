# Get user input
name = input("Enter your name: ")
hobby = input("What's your favourite hobby?")

greeting = "Hello!", name, "It's a pleasure to meet you!"
welcome = "It's great that you love" + hobby.lower() + "!"

# print results

print(greeting)
print(welcome)
print("Your name in uppercase is " + name.upper() + "!")
print("Your name has", len(name), "letters.")
print("The first letter of your hobby is:", hobby[0])
