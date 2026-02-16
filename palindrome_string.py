# Palindrome Checker Program
# Description: Checks if a string is a palindrome

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False

def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True



    ## TOW Pointer Approach
    def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False
