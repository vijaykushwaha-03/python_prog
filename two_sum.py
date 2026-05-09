def two_sum(nums,target):
    seen = {}
    
    for i,num in enumerate(nums):
        need = target - num
        
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    
    return []
    
nums = [1,2,3,4,5,6]
target = 6

print(two_sum(nums,target))
