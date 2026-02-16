# List Operations Program
# Description: Remove duplicates from list, reverse it, and swap first & last elements

nums = [1, 2, 2, 3, 4, 4, 5]
rs = list(set(nums))
print(rs)
print(type(rs))
print(rs[::-1])

rs[0],rs[-1] = rs[-1], rs[0]
print(rs)
