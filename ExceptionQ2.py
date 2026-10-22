try:
    a = int(input("Enter a number:"))
except:
    print("Enter a valid number")
else:
    print("You entered ",a)
finally:
    print("Successful")
