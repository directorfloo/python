def display_unique(words):
    normalized = [word.lower() for word in words]
    unique_words = set(normalized)
   sorted_words = sorted(unique_words)
    print("Unique words in alphabetical order:")
    for word in sorted_words:
        print(word)


sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Python is fun and python is powerful"
sentence3 = "Apple banana orange apple Banana grape"

# split into words and test
display_unique(sentence1.split())
print()
display_unique(sentence2.split())
print()
display_unique(sentence3.split())
