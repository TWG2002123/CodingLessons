# Day 7 Problems

# Sum of all the even numbers

total = 0
for i in range (1,11):
    if i % 2 == 0: 
        total += i 
print("Sum of even numbers", total)

#print name multiple times

name = input("please enter your name: ")
count = int(input("please enter a number (1-5): "))
for i in range (count):
    print (name)

#Problem 3: Check Grade

score = float(input("Enter a number between (0-100): " ))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C or below"
print("your grade is:", grade)
