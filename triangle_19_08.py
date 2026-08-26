# create a class triangle with 3 variables side1, side2, side3. initialise the variables with constructor .
# it also has angle1, , angle2 , angle3 . all sides and angles will be initialised with constructor
# create a class equilateral triangle and find the area of triangle with cal_area func . find the tangent of all angles using  find_ angle()
# create scalene class which is child of triangle class . find perimeter of trianlge with cal_perimeter()
# print area  as a whole no . NO TYPECASTING . USE MATH PCKG

import math

class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

class Equilateral(Triangle):
    def calarea(self):
        area = (math.sqrt(3) / 4) * math.pow(self.side1, 2)
        print("Area:", area)

    def find_angle(self):
        print("Tan Angle 1:", math.tan(math.radians(self.angle1)))
        print("Tan Angle 2:", math.tan(math.radians(self.angle2)))
        print("Tan Angle 3:", math.tan(math.radians(self.angle3)))

class Scalene(Triangle):
    def calperimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print("Perimeter:", perimeter)

    def calarea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s-self.side1) * (s-self.side2) * (s-self.side3))
        print("Area:", area)


e = Equilateral(6, 6, 6, 60, 60, 60)
e.calarea()
e.find_angle()

sc = Scalene(5, 6, 7, 40, 60, 80)
sc.calperimeter()
sc.calarea()