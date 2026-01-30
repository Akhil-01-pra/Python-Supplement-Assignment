# Problem 99: Find maximum subarray sum
# Find and fix the error

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
print(f"Maximum subarray sum: {max_subarray_sum(numbers)}")
