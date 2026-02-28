
# BMI Calculator Program
# This program calculates BMI (Body Mass Index) and classifies it into different health categories.

# Taking input from user
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculating BMI using formula
# BMI = weight / (height^2)
bmi = weight / (height * height)

# Displaying BMI value rounded to 2 decimal places
print("\nYour BMI is:", round(bmi, 2))

# BMI Classification using AND operator
if bmi < 18.5:
    print("Category: Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Category: Healthy")

elif bmi >= 25 and bmi < 30:
    print("Category: Overweight")

else  :
    print("Category : obese")

    

# End message
print("\nThank you for using the BMI Calculator!")