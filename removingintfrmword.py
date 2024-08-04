print("vv"*30)
text = input("Enter the text: ")

# Remove digits from the text
cleaned_text = ''.join([char for char in text if not char.isdigit()]).upper()

print("text:", cleaned_text)

print("@"*30)
#-----------------------------------------------------------------------------------------------------
for char in text.lower():
    if not char.isdigit():
        print(char, end='')

# Filter out characters that are not alphanumeric and not spaces
cleaned_text = ''.join(filter(lambda char: char.isalnum() or char.isspace() or char.isdigit(), text))

print("Text without special characters:", cleaned_text)
print("^^"*30)