# Problem 65: Check if list has duplicates
# Find and fix the error

def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False
print(f"Has duplicates: {has_duplicates(numbers)}")
