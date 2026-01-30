# Problem 72: Count uppercase and lowercase letters
# Find and fix the error

def count_case(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count 
print(f"Uppercase: {u}, Lowercase: {l}")
