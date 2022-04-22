'''Define a class named “Polygon”. The number of sides of the polygon should be a parameter of
the constructor of class. This class should implement 2 methods:
a. “inputSides”: iteratively ask the user to input the length of each polygon side
b. “dispSides”: prints the index and the length of each polygon size'''

class polygon:
    def __init__(self,totalsides):
        self.totalsides=totalsides
        self.sides=[]
    def inputsides(self):
        for i in range(self.totalsides):
            self.sides.append(int(input("please enter the length of sides in cm:")))

    def dispsides(self):
        for index,side in enumerate(self.sides):
            print("Index : {}  Side:{}".format(index,side))

if __name__=="__main__":
    t1 = polygon(int(input("Enter the number of sides up to 360:")))
    t1.inputsides()
    t1.dispsides()