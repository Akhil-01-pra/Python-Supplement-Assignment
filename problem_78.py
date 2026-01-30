# Problem 78: Find duplicate elements in list
# Find and fix the error

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


print(f"Duplicates: {find_duplicates(numbers)}")
