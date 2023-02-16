# while loop guessing game
'''
secret_nr = 5
guess_coumt = 0
guess_limit = 3
while guess_coumt < guess_limit:
    guess = int(input(f'Your {guess_coumt + 1} guess: '))
    guess_coumt += 1
    if guess == secret_nr:
        print("That's right!")
        break
else:
    print("Not this time!")
'''
# car simulation game
command = ''
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print('''Type:
        start - to start the car
        stop - to stop the car
        quit - to exit''')
    elif command == "start":
        print("The engine starts.")
    elif command == "stop":
        print("The engine stops.")
    elif command == "quit":
        break
    else:
        print("I can't execute this command.")