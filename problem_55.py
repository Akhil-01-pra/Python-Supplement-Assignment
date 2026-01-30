# Problem 55: Count frequency of each element
# Find and fix the error

def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
print(f"Frequency: {count_frequency(numbers)}")
