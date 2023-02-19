try:
    age = int(input('Age: '))
    income = 1600
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age must be greater than 0')
except ValueError:
    print('Invalid value')