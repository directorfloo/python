result = list(filter(lambda digit: digit % 3 == 0 and digit % 5 == 0, range(1, 51)))

print(result)