try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c = a / b
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(c)
finally:
    print("Successful")
