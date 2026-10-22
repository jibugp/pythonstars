numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter an index (0-4): "))
except:
    print("Index is out of range.")
else:
    print("Element:", numbers[index])
finally:
    print("Successful")
