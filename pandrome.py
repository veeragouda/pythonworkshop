
def is_palindrome(sequence):
    return sequence == sequence[::-1]

# Example usage
n = input( " enter the number :", )
if is_palindrome(n):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")