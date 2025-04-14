# BMI = weight (kg) / (height (m)²)

# Input name, weight, height → calculate BMI → check category → print result → loop to restart.

# Get user input 

name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres: "))

# calculate BMI
bmi = weight / (height * height)

# Assign to a category

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal"
elif bmi < 30:
    category = "overweight"
else: 
    category = "obese"

print("Hey", name, "Your BMI is", round(bmi, 2), "-", category)
print()
