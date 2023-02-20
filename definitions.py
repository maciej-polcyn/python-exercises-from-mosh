def appreciate_effort():
    print('You just defined your first function!')
    print("You'll soon write amazing codes!")


def greet_user(first_name, last_name):  # name is a parameter of the function
    print(f'''
Hi {first_name} {last_name},
Welcome aboard!
    ''')


def square(number):
    number = number * number
    return number


print(square(4))
def fizz_buzz(number):
    output = ''
    if number % 3 == 0:
        output = 'Fizz'
        if number % 5 == 0:
            output = 'FizzBuzz'
    elif number % 5 == 0:
        output = 'Buzz'
        if number % 3 == 0:
            output = 'FizzBuzz'
    else:
        output = number
    return output


# print(square(4))

# greet_user(
#     last_name='Polcyn',
#     first_name='Maciej')  # keyword arguments - position doesn't matter

<<<<<<< HEAD
=======
print(fizz_buzz(15))


>>>>>>> 6923062 (Merging the files.)
