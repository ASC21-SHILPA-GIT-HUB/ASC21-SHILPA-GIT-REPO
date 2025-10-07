def word_count(text):
    words = text.split()
    return len(words)

# --- Test ---
sentence = "Sum of 12 and 20 is 32"
print("Input:", sentence)
print("Word Count:", word_count(sentence))
