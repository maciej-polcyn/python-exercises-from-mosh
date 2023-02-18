# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# list methods
numbers = [3, 5, 7, 6, 4, 23, 54, 6, 10]
numbers_copy = numbers.copy()
unique_nr = []

numbers.insert(5, 17)
numbers.sort()

numbers_copy.append(17)
numbers_copy.reverse()

for index in numbers:
    if index not in unique_nr:
        unique_nr.append(index)

print(numbers.pop(5))
print(numbers.count(6))
print(numbers)
print(numbers_copy)
print(unique_nr)