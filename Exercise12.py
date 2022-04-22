'''Overload the “__add__” operator of the “EquilateralTriangle” class in order to use “+” operator
to perform the sum of the perimeters of two instances of “EquilateralTriangle” class'''

class EquilateralTriangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    #adding two objects
    def __add__(self, o):
        return (self.a+o.a)+(self.b+o.b)+(self.c+o.c)
obj1= EquilateralTriangle(3,3,3)
obj2= EquilateralTriangle(5,5,5)
print(obj1+obj2)