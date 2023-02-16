# while loop guessing game
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
