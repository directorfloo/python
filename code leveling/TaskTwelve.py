words = ['level', 'world', 'madam', 'python']

palindromes = list(filter(lambda words: words == words[::-1], words))

print(palindromes)