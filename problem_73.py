# Problem 73: Find maximum difference between elements
# Find and fix the error

def max_difference(lst):                
    if len(lst) < 2:
        return 0
    min_elem = lst[0]
    max_diff = lst[1] - lst[0]
    for i in range(1, len(lst)):
        if lst[i] - min_elem > max_diff:
            max_diff = lst[i] - min_elem
        if lst[i] < min_elem:
            min_elem = lst[i]
    return max_diff
print(f"Max difference: {max_difference(numbers)}")
