a = "Doug"
b = 22
c = 1984


def rotate(x, y, z):
    
    return (z, x, y)   
a, b, c = "Doug", 22, 1984

# call 1
a, b, c = rotate(a, b, c)
print("After call 1:", a, b, c)

# call 2
a, b, c = rotate(a, b, c)
print("After call 2:", a, b, c)

# call 3
a, b, c = rotate(a, b, c)
print("After call 3:", a, b, c)
