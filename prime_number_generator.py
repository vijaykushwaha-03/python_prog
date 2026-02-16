# Prime Number Generator Program
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
