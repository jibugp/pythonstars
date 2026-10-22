class Person:
    def __init__(self):
        self.__age = 0
    def set_age(self, age):
        if age > 0:
            self.__age = age
            print("Age updated successfully")
        else:
            print("Age must be positive")
    def get_age(self):
        return self.__age
p = Person()
p.set_age(25)
print(p.get_age())
p.set_age(-5)
