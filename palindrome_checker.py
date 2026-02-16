# Palindrome Checker Program
# Description: Checks if a string is a palindrome

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False
