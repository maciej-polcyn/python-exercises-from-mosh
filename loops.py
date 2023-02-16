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
start_condition = input("Do you wanna play a car game? Y/N ")
while start_condition.upper() == "Y":
    action = input("Type:"
          "\nstart - to start the car"
          "\nstop - to stop the car"
          "\nquit - to exit\n"
    )
    if action == "start":
        print("The engine starts.")
    elif action == "stop":
        print("The engine stops.")
    elif action == "quit":
        break
        # start_condition = False
    else:
        print("I can't execute this command.")