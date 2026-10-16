p = 4
for i in range(5):
    for space in range(p):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
    p = p - 1