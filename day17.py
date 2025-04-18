# Greet user function with default and keyword arguments
def greet(name, message = "Hello"):
    return f"{message}, {name}!"

name  =  input("Please enter your name: ")
print(greet(name))
print(greet(name, "Welcome"))
print(greet(name = name, message = "Hi"))

name  =  input("Please enter your name: ")
print(f"Hey {name}, nice to meet you. Let's try some greetings")

def greet(name, message = "Hello", title = ""):
    return f"{message}, {title}{name}!".strip()

while True:
    message = input("Enter a greeting message (or press enter for 'Hello'): " )
    if message == "":
        message = "Hello"
    
    title = input("Enter your title eg Mr., Dr., (or press 'Enter' to skip): ")
    
    if message.lower() == "quit" or title.lower() == "quit":
        print(f"Goodbye {name}!")
        break
    
    result = greet(name = name, message = message, title = title)
    print(result)

    print(f"That's like welcoming a Liverpool fan {name}" if "welcome" in message.lower() else f"Great greeting {name}, A great way to keep the anfield spirit up")


    
    
