# Problem 77: Check if number is perfect square
# Find and fix the error

def is_perfect_square(n):
    if n < 0:
        return False
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared == n:
            return True
        elif mid_squared < n:
            left = mid + 1
        else:
            right = mid - 1
    return False

print(f"Is 16 perfect square? {is_perfect_square(16)}")
print(f"Is 15 perfect square? {is_perfect_square(15)}")
