gender = input ("What's your gender? M/K ")
weight = input('How much do you weight in kg? ')
height = input("what's your height in cm? ")
age = input("How old are you? ")
bmr = round(88.362 + (13.397 * int(weight)) + (4.799 * int(height)) - (5.677 * int(age)))

print(f"Your Basal Metabolic Rate equals {bmr} kcal.")