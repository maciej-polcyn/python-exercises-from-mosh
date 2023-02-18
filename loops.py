# while loop guessing game
#
# secret_nr = 5
# guess_coumt = 0
# guess_limit = 3
# while guess_coumt < guess_limit:
#     guess = int(input(f'Your {guess_coumt + 1} guess: '))
#     guess_coumt += 1
#     if guess == secret_nr:
#         print("That's right!")
#         break
# else:
#     print("Not this time!")


# while loop car simulation game

# engine_running = False
# while True:
#     command = input("> ").lower()
#     if command == "help":
#         print('''
# Type:
# start - to start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif command == "start":
#         if engine_running:
#             print("The engine is already running.")
#         else:
#             print("The engine starts.")
#             engine_running = True
#     elif command == "stop":
#         if engine_running:
#             print("The engine stops.")
#             engine_running = False
#         else:
#             print("The engine is not running.")
#     elif command == "quit":
#         break
#     else:
#         print("I can't execute this command.")

# for loop
# prices = [10, 20, 30]
# cart = 0
# for item in prices:
#     cart += item
# print(cart)

# nested loops

# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# numbers = [2,2,2,2,5]
# for row in numbers:
#     printer = ''
#     for x in range(row):
#         printer += "X"
#     print(printer)

numbers = [0,6,4,3,2,56,76,34,6,54,98,90,98,55,1]
biggest_nr = 0
for i in numbers:
    if i > biggest_nr:
        biggest_nr = i
print(biggest_nr)