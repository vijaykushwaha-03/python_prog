

def sec_larg(nums):
    if len(nums) < 2:
        return -1 
        
    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
            
        elif first > num > second:
            second = num
            
        
    return second if  second !=  float('-inf') else -1 
    
    
print(sec_larg([1, 8, 3, 4, 7]))        # 4
