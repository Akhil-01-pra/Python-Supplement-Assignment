# Problem 66: Find intersection of two lists
# Find and fix the error

def intersection(list1, list2):
    return list(set(list1) & set(list2)) 
print(f"Intersection: {intersection(l1, l2)}")
