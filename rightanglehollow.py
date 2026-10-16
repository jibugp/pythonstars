for i in range(1,6):
    for j in range(1,6):
        if i == j:
            print("*", end=" ")
        elif i == 5:
            print("*", end=" ")
        elif j == 1:
            print("*", end=" ")    
        else:
            print(" ", end=" ")
    print()