# Vowel Counter Program
# Description: Counts the number of vowels in a string

def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("hello world"))  # 3
