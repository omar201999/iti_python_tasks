import math


class Shape:
    count = 0

    def __init__(self, name, color, d1, d2):
        self.name = name
        self.color = color
        self.d1 = d1
        self.d2 = d2
        Shape.count += 1

    def area(self):
        return (self.d1) * (self.d2)

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Dimensions: {self.d1} x {self.d2} , Area = {self.area()}"


class Circle(Shape):
    count = 0

    def __init__(self, rad, color):
        super().__init__("Circle", color, rad * 2, rad * 2)
        self.rad = rad
        Circle.count += 1

    def area(self):
        return (math.pi) * (self.rad) * (self.rad)


# Creating objects
shape1 = Shape("Rectangle", "Blue", 4, 6)
shape2 = Shape("Square", "Red", 5, 5)
circle1 = Circle(3, "Green")

# Printing objects and counts
print(str(shape1))
print(f"Rectangle Area = {shape1.area()}")
print("#" * 50)
print(f"Square Area = {shape2.area()}")
print(str(shape2))
print("#" * 50)
print(f"Circle Area = {circle1.area()}")
print("#" * 50)
print(f"Number of shapes created: {Shape.count}")
print("#" * 50)
print(f"Number of circles created: {Circle.count}")
