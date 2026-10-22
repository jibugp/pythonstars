student = {"name": "J", "age": 27, "course": "Python"}
try:
    key = input("Enter a key (name, age, course): ")
except:
    print("The key does not exist.")
else:
    print("Value:", student[key])
finally:
    print("Successful")
