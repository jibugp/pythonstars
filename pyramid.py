p = 3
star = 1
for i in range(1,5):
    for space in range(p):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    print()
    p = p - 1
    star = star + 2
