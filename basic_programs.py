def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # olleh

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(find_largest([1, 8, 3, 4]))  # 8


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

print(fibonacci(5))  # [0, 1, 1, 2, 3]


def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("hello world"))  # 3
