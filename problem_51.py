# Problem 51: Reverse words in a sentence
# Find and fix the error

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words       
print(f"Reversed words: {reverse_words(text)}")
