for i in range(5):
    for j in range(9):
        if i == 4:
            print("*", end=" ")
        elif j == 4 + i:
            print("*", end=" ")
        elif j == 4 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(5):
    for j in range(9):
        if i == 4:
            print("*", end=" ")
        elif j == 0:
            print("*", end=" ")
        elif j == 8:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()