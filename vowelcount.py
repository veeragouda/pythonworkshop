text = input("Enter the word: ")
vowel_count = {}  # Dictionary to store vowel counts

for i in text:
    if i in "aeiouAEIOU":  # Check if the character is a vowel
        i = i.lower()  # Convert to lowercase for consistent counting
        if i in vowel_count:
            vowel_count[i] += 1  # Increment count if vowel is already in the dictionary
        else:
            vowel_count[i] = 1  # Initialize count if vowel is not in the dictionary

# Print the result
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")

print("Total number of vowels:", sum(vowel_count.values()))
