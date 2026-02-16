# Find Largest Number Program (Version 2)
# Description: Finds the largest number in a list using index-based loop

def largest(n):
    larg = n[0]
    for i in range(len(n)):
        if n[i] > larg:
            larg = n[i]
    return (larg)

print(largest([10, 20, 45, 5]))
