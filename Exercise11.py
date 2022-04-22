''' Define a subclass of “Triangle” named “EquilateralTriangle”. This class should override the
“findPerimeter” method to print the perimeter of the triangle by just evaluating 3 times the
length of one of its side rather than their sum.'''

class Triangle:
    def FindPerimeter(self,x,y,z):
        return(x+y+z)*3
class EquilateralTriangle(Triangle):
    def EquilateralTriangle(self,x,y,z):
        return (x+y+z)*3
print("Enter Length of all the three sides:",end="")
a=float(input())
b=float(input())
c=float(input())

object1= Triangle()
object2= EquilateralTriangle()
p=object2.FindPerimeter(a,b,c)
print("\nPerimeter={:2f}".format(p))

