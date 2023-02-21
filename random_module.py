import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

the_office = ['Mike', 'Kevin', 'Creed', 'Oscar', 'Dwight', 'Jim', 'Ryan',
         'Tobey', 'Daryl', 'Pam', 'Angela', 'Phyllis', 'Kelly']
leader = random.choice(the_office)
print(leader)

