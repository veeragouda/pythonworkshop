#
# def get_initials(full_name):
#     return " ".join(f"{name[0]}." for name in full_name.split())
#
# print(get_initials("James Clerk Maxwell"))
#

def get_initials(name):
    # Split the name into words
    words = name.split()
    # Take the first letter of each word and join them together
    initials = ''.join(word[0] for word in words)
    return initials.upper()  # Convert to uppercase for consistency

# Example usage
name =input(" enter the name :'' ")
initials = get_initials(name)
print("Initials:", initials)