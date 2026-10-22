class Shape:
    def display(self):
        print("Shape")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Circle area =", 3.14 * self.radius * self.radius)
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print("Rectangle area =", self.length * self.breadth)
c = Circle(10)
c.display()
c.area()
r = Rectangle(10, 5)
r.display()
r.area()
