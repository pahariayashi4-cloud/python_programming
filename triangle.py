#create a class shape with a variable radius. initialise the varible with constructr . create a class circld  witch is schild of shape class
#define a method cal_area() to cal area using math pckg. 
# create a class shperre which is child of shape class . define cal_volume to finf volume of sphere 


#create a class triangle with 3 variables side1, side2, side3. initialise the variables with constutor .
# #it also has angle1, , angle2 , angle3 . all sides an angles will be initialised with constructor
# c create a class equilatersla trainalgek and find the area of triangle with cal area func . find the tangent of all angles using  find_ angle() 
#create scalene class wivh is child of triangle class . find perimeter of trianlge with cal_perimeter() 
#print area  as a whole no . NO TYPECASTING . USE MATH PCKG


'''import math

class Shape:
    def __init__(self, r):
        self.r = r


class Circle(Shape):
    def cal_area(self):
        area = math.pi * self.r * self.r
        print("Area of Circle =", area)


class Sphere(Shape):
    def cal_volume(self):
        volume = (4 / 3) * math.pi * self.r* self.r * self.r
        print("Volume of Sphere =", volume)


# Creating objects
c = Circle(5)
c.cal_area()

s = Sphere(5)
s.cal_volume()
'''

import math

class Triangle:
    def __init__(self, s1, s2, s3, a1, a2, a3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


class EquilateralTriangle(Triangle):
    def cal_area(self):
        area = (math.sqrt(3) / 4) * self.s1 * self.s1
        print("Area of Equilateral Triangle =", area)

    def find_angle(self):
        print("Tangent of angle 1 =", math.tan(math.radians(self.a1)))
        print("Tangent of angle 2 =", math.tan(math.radians(self.a2)))
        print("Tangent of angle 3 =", math.tan(math.radians(self.a3)))


class ScaleneTriangle(Triangle):
    def cal_perimeter(self):
        perimeter = self.s1 + self.s2 + self.s3
        print("Perimeter of Scalene Triangle =", perimeter)


# Creating object of Equilateral Triangle
e = EquilateralTriangle(6, 6, 6, 60, 60, 60)

e.cal_area()
e.find_angle()


# Creating object of Scalene Triangle
s = ScaleneTriangle(5, 6, 7, 50, 60, 70)

s.cal_perimeter()