# Problem 97: Remove element from list
# Find and fix the error

def remove_element(nums, val):
    length = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[length] = nums[i]
            length += 1
    return length
    
print(f"New length: {length}")
print(f"Modified list: {numbers[:length]}")
