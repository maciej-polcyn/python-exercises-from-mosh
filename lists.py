# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# list methods
# numbers = [3, 5, 7, 6, 4, 23, 54, 6, 10]
# numbers_copy = numbers.copy()
# unique_nr = []
#
# numbers.insert(5, 17)
# numbers.sort()
#
# numbers_copy.append(17)
# numbers_copy.reverse()
#
# for index in numbers:
#     if index not in unique_nr:
#         unique_nr.append(index)
#
# print(numbers.pop(5))
# print(numbers.count(6))
# print(numbers)
# print(numbers_copy)
# print(unique_nr)

# Tuples - cannot be modified

# this_is_tuple = (1,2,3,4,5,6)
# print(this_is_tuple.count(3))
# print(this_is_tuple.index(5))

# Unpacking lists or tuples
numbers = [1, 2, 3]
x, y, z = numbers

names = ['Mike', 'Kevin','Creed', 'Oscar', 'Dwight', 'Jim', 'Ryan',
         'Tobey', 'Daryl', 'Pam', 'Angela', 'Phyllis', 'Kelly']
names.sort()
a, b, c, d, e, f, g, h, i, j, k ,l, m = names

print(x, y, z)
print(a, b, c)