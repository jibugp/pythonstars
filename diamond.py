a = 2
star = 1
for i in range(3):
    for space in range(a):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    print()
    a = a - 1
    star = star + 2
b = 1
star = 3
for i in range(2):
    for space in range(b):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    print()
    b = b + 1
    star = star - 2