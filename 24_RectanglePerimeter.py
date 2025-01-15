class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        self.area = self.length*self.breadth
        print("The area of the rectangle is:",self.area)
        return self.area

    def getPerimeter(self):
        self.perimeter = 2*(self.length + self.breadth)
        print("The perimeter of the rectangle is:",self.perimeter)
        return self.perimeter

length1 = int(input("Enter the length of the 1st rectangle:"))
breadth1 = int(input("Enter the breadth of the 1st rectangle:"))
rect1 = Rectangle(length1,breadth1)
area1 = rect1.getArea()
rect1.getPerimeter()
length2 = int(input("Enter the length of the 2nd rectangle:"))
breadth2 = int(input("Enter the breadth of the 2nd rectangle:"))
rect2 = Rectangle(length2,breadth2)
area2 = rect2.getArea()
rect2.getPerimeter()
if(area1==area2):
    print("The area of both the rectangles are the same.")
elif(area1>area2):
    print("The area of the 1st rectangle is greater than the 2nd one.")
else:
    print("The area of the 1st rectangle is lesser than the 2nd one.")

