# Sum of even numbers from 1-20

total = 0
for i in range (1, 21):
    if i % 2 == 0:
        total += i 
print("Sum of even numbers from 1-20: ", total)

name = input("Please enter your name: ")
print(f"Hey {name}, Let's do a sum of all the even numbers from 1-20")

total = 0
even_numbers = []
for i in range (1, 21):
    if i % 2 == 0:
        total += i
        even_numbers.append(i) #store the even numbers

print(f"Hey {name}, the even numbers are {even_numbers}")
print(f"The sum of the even numbers is {total}")
