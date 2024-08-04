
numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# count = 0
#
# # Counting elements in the list
# for i in numbers:
#     count += 1
#
# print("Count of numbers:", count)

# Create a range from 1 to 9 (inclusive)
list1 = range(1, 10)

# Find the missing numbers by using set difference
missing_numbers = set(list1) - set(numbers)
print("Missing numbers:", missing_numbers)