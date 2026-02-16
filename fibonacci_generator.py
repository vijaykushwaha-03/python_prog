# Fibonacci Sequence Generator Program
# Description: Generates Fibonacci sequence up to n numbers

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

print(fibonacci(5))  # [0, 1, 1, 2, 3]
