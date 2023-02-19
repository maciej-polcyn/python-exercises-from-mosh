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

# greet_user(
#     last_name='Polcyn',
#     first_name='Maciej')  # keyword arguments - position doesn't matter

