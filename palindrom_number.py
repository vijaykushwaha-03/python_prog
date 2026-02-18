def is_pali(n):
    if n < 0:
        return False
        
    orig = n
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    
    return orig == rev
    
print(is_pali(121))