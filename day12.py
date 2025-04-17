name = input("Please enter your name: ")
print(f"Let's manage your shopping list together {name}!")

shopping_list = ["milk", "bread", "eggs"]

while True:
    print("\nYour shopping list: ")
    for i in range(len(shopping_list)):
        print(f"{i+1}. {shopping_list[i]}")

    action = input("\nType 'add' to add 'remove' to remove or 'quit': ").lower()

    if action == 'quit':
        print(f"Hey {name}, Your final shopping list is: ", shopping_list)
        break
    elif action == 'add':
        item = input("Please add your item: ")
        shopping_list.append(item)
        print(f"You successfully added: ", {item})
    elif action == 'remove':
        item = input("Please enter the item you would like to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"You succesfully removed: ", {item})
        else:
            print(f"{item} is not in the list")
    else:
        print("Incorrect input. Please enter either 'add', 'remove' or 'quit")
print("Goodbye!")
