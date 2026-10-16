for i in range(5):
    for j in range(5):
        if i==4:
            print("*", end=" ")
        elif j==4:
            print("*", end=" ")
        elif j==4-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()