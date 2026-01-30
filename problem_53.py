# Problem 53: Check if two strings are anagrams
# Find and fix the error

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2) 
print(f"Are anagrams: {are_anagrams(word1, word2)}")
