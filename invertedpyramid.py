p = 0
star = 7
for i in range(5):
    for space in range(p):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    print()
    p = p + 1
    star = star - 2