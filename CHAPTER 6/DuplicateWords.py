def count_duplicates(sentence):
    
    words = sentence.lower().split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    duplicates = {word: count for word, count in counts.items() if count > 1}

  
    if duplicates:
        print("Duplicate words and their counts:")
        for word, count in duplicates.items():
            print(f"{word}: {count}")
    else:
        print("No duplicate words found.")



sentence = "This is a test This test is only a test"
count_duplicates(sentence)
