# ==================== PROGRAM 1: STRING REVERSAL ====================
# Description: Reverses a given string using slicing

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # olleh


# ==================== PROGRAM 2: PALINDROME CHECKER ====================
# Description: Checks if a string is a palindrome

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))  # True
print(is_palindrome("hello"))  # False


# ==================== PROGRAM 3: FACTORIAL CALCULATOR ====================
# Description: Calculates factorial of a number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


# ==================== PROGRAM 4: FIND LARGEST NUMBER (VERSION 1) ====================
# Description: Finds the largest number in a list using for-each loop

def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(find_largest([1, 8, 3, 4]))  # 8


# ==================== PROGRAM 5: FIBONACCI SEQUENCE GENERATOR ====================
# Description: Generates Fibonacci sequence up to n numbers

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

print(fibonacci(5))  # [0, 1, 1, 2, 3]


# ==================== PROGRAM 6: VOWEL COUNTER ====================
# Description: Counts the number of vowels in a string

def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("hello world"))  # 3


# ==================== PROGRAM 7: PRIME NUMBER GENERATOR ====================
# Description: Prints all prime numbers from 1 to n (user input)

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

n = int(input("Enter Number =>"))

for num in range(1,n+1):
    if isPrime(num):
        print(num, end=" ")


# ==================== PROGRAM 8: LIST OPERATIONS ====================
# Description: Remove duplicates from list, reverse it, and swap first & last elements

nums = [1, 2, 2, 3, 4, 4, 5]
rs = list(set(nums))
print(rs)
print(type(rs))
print(rs[::-1])

rs[0],rs[-1] = rs[-1], rs[0]
print(rs)


# ==================== PROGRAM 9: FIND LARGEST NUMBER (VERSION 2) ====================
# Description: Finds the largest number in a list using index-based loop

def largest(n):
    larg = n[0]
    for i in range(len(n)):
        if n[i] > larg:
            larg = n[i]
    return (larg)

print(largest([10, 20, 45, 5]))