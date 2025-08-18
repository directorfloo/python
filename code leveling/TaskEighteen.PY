from functools import reduce

letter = ['I', 'love', 'Python']

sentence = reduce(lambda x, y: x + " " + y, letter)

print(sentence)