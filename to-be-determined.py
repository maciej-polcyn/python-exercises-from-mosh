# BMR Calculator

gender = input ("What's your gender? M/K ")
weight = input('How much do you weight in kg? ')
height = input("what's your height in cm? ")
age = input("How old are you? ")
bmi = round(int(weight)/(int(height)/ 100)**2, 2)
evaluation = ''
if gender.upper() == 'M':
    bmr = round(88.362 + (13.397 * int(weight)) + (4.799 * int(height)) - (5.677 * int(age)), 2)
else:
    bmr = round(447.593 + (9.247 * int(weight)) + (3.098 * int(height)) - (4.330 * int(age)), 2)

if bmi < 18.5:
    evaluation = 'you have an underweight.'
elif bmi >= 18.5 and bmi <= 24.9:
    evaluation = 'your weight is just right.'
elif bmi > 24.9 and bmi < 30:
    evaluation = 'you have an overweight.'
else:
    evaluation = 'you are extremely obese.'


print(f"Your Basal Metabolic Rate equals {bmr} kcal. \nYour BMI is {bmi}. That means {evaluation}")
