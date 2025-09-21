def letter_summary():
   
    sentence = input("Enter a sentence: ")

   
    sentence = sentence.lower().replace(" ", "")

    counts = {}
    for ch in sentence:
        counts[ch] = counts.get(ch, 0) + 1

    print("\nLetter  Count")
    print("--------------")
    for letter in sorted(counts.keys()):
        print(f"{letter:^6}  {counts[letter]}")

    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set(sentence)
    missing = alphabet - used_letters

    print("\nLetters not used:")
    print(" ".join(sorted(missing)) if missing else "All letters used!")


letter_summary()
