#Create a class Shape with a variable radius.
# Initialize the variable with constructor.
# Create a class Circle which is the child of Shape class.
# Define a method calarea() to calculate the area of circle using math package.
#Create a class Sphere which is a child of Shape class. Define calvolume() to calculate the volume of the sphere.


import math

class Shape:
    def __init__(self, radius):
        self.radius = radius

class Circle(Shape):
    def calarea(self):
        area = math.pi * math.pow(self.radius, 2)
        print("Area of Circle:", area)

class Sphere(Shape):
    def calvolume(self):
        volume = (4/3) * math.pi * math.pow(self.radius, 3)
        print("Volume of Sphere:", volume)


c = Circle(5)
c.calarea()

s = Sphere(5)
s.calvolume()