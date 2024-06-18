def count_word_occurrences(text, word):
    """Counts the occurrences of a word in a given text."""
    lower_text = text.lower()
    words = lower_text.split()
    word_count = 0
    for w in words:
        if w == word:
            word_count += 1
    return word_count
text = "This is a sample text with the word 'word' appearing multiple times."
target_word = "word"

word_count = count_word_occurrences(text, target_word)
print(f"The word '{target_word}' occurs {word_count} times in the text.")
