"""Define now a subclass of “Polygon” named “Triangle”. In this case the number of sides of the
triangle must not be a parameter of the class. This class should implement the following
methods:
a. “findPerimeter”: prints the sum of the sides and stores it in a variable
b. “findArea”: starting from the length of the sides it should print the area of the triangle
(formula: area = (s * (s - a) * (s - b) * (s - c)) ** 0.5) where s is the semi-perimeter and
a,b,c are the sides of the triangle
"""

class polygon: #superclass
    def __init__(self,totalsides):
        self.totalsides=totalsides
        self.sides=[]
    def inputsides(self):
        for i in range(self.totalsides):
            self.sides.append(int(input("please enter the length of sides:")))

    def dispsides(self):
        for index,side in enumerate(self.sides):
            print("Index : {}  Side:{}".format(index,side))

class Triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)

    def perimeter(self):
        return sum(self.sides)

    def get_area(self):
        a,b,c=self.sides
        s=(a+b+c)
        area= (s*(s-a)*(s-b)*(s-c))**0.5
        return area
if __name__=="__main__":
    t1=Triangle()
    t1.inputsides()
    t1.perimeter()
    area=t1.get_area()
    print("perimeter of triangle is {}: (cm)".format(t1.perimeter()))
    print("Area of triangle is {}".format(area))
