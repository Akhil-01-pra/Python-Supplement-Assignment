# Problem 54: Find nth Fibonacci number
# Find and fix the error

def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a    

print(f"10th Fibonacci number: {nth_fibonacci(10)}")
