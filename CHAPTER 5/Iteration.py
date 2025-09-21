
table = [[0 for col in range(3)] for row in range(2)]

count = 1

for row in range(2):         
    for col in range(3):   
        table[row][col] = count
        count += 1

print("   ", end="")
for col in range(3):
    print(f"{col:^5}", end="")   
print()


for row in range(2):
    print(f"{row} |", end=" ")
    for col in range(3):
        print(f"{table[row][col]:^5}", end="")
    print()
