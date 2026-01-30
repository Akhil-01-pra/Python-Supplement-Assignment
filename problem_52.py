# Problem 52: Find missing number in sequence
# Find and fix the error

def find_missing(numbers):
    n = len(numbers) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return total_sum - actual_sum       
print(f"Missing number: {find_missing(nums)}")
