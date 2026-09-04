words = input("Enter words: ").split()


def word_length(word):
    return len(word)


# a) Find length of every word
lengths = list(
    map(lambda word: (word, len(word)), words)
)

# b) Extract words having more than 5 characters
long_words = list(
    filter(lambda word: len(word) > 5, words)
)

# c) Sort according to length
sorted_words = sorted(
    words,
    key=lambda word: len(word)
)

print("Length of every word:")
print(lengths)

print("\nWords having more than 5 characters:")
print(long_words)

print("\nWords sorted according to length:")
print(sorted_words)