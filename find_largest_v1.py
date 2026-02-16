# Find Largest Number Program (Version 1)
# Description: Finds the largest number in a list using for-each loop

def find_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(find_largest([1, 8, 3, 4]))  # 8
