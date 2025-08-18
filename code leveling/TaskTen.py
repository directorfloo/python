data = [(1, 'A'), (4, 'B'), (2, 'C')]

solution = list(filter(lambda number: number[0] > 2, data))

print(solution)