# BMI CALCULATOR
# print("BMI Calculator")
# height = float(input("Enter your height in m: \n"))
# weight = int(input("Enter your weight in kg: \n"))

# bmi = weight / (height ** 2)

# print("Result: " + str(int(bmi)))


#1 Year days = 365, weeks = 52, months = 12 
# How many Days?
# age = input("What is your current age? ")

# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."

# print(message)


# Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would be like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill+ total_tip_amount
amount = total_bill / people
final_amount = "{:.2f}".format(round(amount, 2))

print(f"Each person should pay: ${final_amount} ")