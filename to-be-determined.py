gender = input ("What's your gender? M/K ")
weight = input('How much do you weight in kg? ')
height = input("what's your height in cm? ")
age = input("How old are you? ")


if gender.upper() == 'M':
    bmr = round(88.362 + (13.397 * int(weight)) + (4.799 * int(height)) - (5.677 * int(age)), 2)
else:
    bmr = round(447.593 + (9.247 * int(weight)) + (3.098 * int(height)) - (4.330 * int(age)), 2)


print(f"Your Basal Metabolic Rate equals {bmr} kcal.")