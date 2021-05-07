#IMPORT

from math import *
# Class

class Line():
    def __init__(self, tup1, tup2):
        self.tup1 = tup1
        self.tup2 = tup2

    def slope(self):
        return (self.tup2[1]-self.tup1[1])/(self.tup2[0]-self.tup1[0])

    def distance(self):
        return sqrt((self.tup2[0]-self.tup1[0])**2 + (self.tup2[1]-self.tup1[1])**2)


line1 = Line((2, 3), (5, 8))

result1 = line1.slope()

print(f"The slope of the given points is {result1}")

result2 = line1.distance()

print(f"\nThe distance between given points is {result2}")