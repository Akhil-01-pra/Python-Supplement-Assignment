# Problem 67: Remove nth element from list
# Find and fix the error

def remove_nth(lst, n):
    if n < 0 or n >= len(lst):
        return lst
    return lst[:n] + lst[n+1:]
print(f"After removing: {result}")
