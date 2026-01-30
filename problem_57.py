# Problem 57: Find LCM of two numbers
# Find and fix the error

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a        

print(f"LCM of 12 and 18: {lcm(12, 18)}")
