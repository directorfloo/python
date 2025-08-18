from functools import reduce
words = ['I', 'love', 'Python']
sentence = reduce(lambda x, y: x**y, words)
[1, 2, 3, 4]