try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c = a / b
except:
    print("Enter a valid number")
else:
    print(c)
finally:
    print("Successful")
