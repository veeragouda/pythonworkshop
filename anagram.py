def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort and compare the strings
    return sorted(str1) == sorted(str2)

# Example usage
word1 = input("enter word : ") #"listen"
word2 = input("enter word : ") #"silent"

if are_anagrams(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')

