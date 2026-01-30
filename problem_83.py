# Problem 83: Find kth smallest element
# Find and fix the error

def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]
print(f"3rd smallest: {kth_smallst(numbers, 3)}")
