numbers = [1, 2, 3, 4, 5, 7, 8, 9]

# Create a range from 1 to 9 (inclusive)
list1 = range(1, 10)

# Find the missing numbers by checking each number in the range
missing_numbers = []
for i in list1:
    if i not in numbers:
        missing_numbers.append(i)

print("Missing numbers:", missing_numbers)

