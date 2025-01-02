class Rectangle:
    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth
        
    def show_len(self):
        print(f"The length of the rectangle is: {self.__length}")
        
    def show_bre(self):
        print(f"The breadth of the rectangle is: {self.__breadth}")
        
    def getArea(self):
        return self.__length*self.__breadth

    def __lt__(self,other):
        return self.getArea()<other.getArea()

length1 = int(input("Enter the length of the first rectangle: "))
breadth1 = int(input("Enter the breadth of the first rectangle: "))
length2 = int(input("Enter the length of the second rectangle: "))
breadth2 = int(input("Enter the breadth of the second rectangle: "))
rect1 = Rectangle(length1,breadth1)
rect2 = Rectangle(length2,breadth2)
print("The area of the first rectangle is:",rect1.getArea())
print("The area of the second rectangle is:",rect2.getArea())
if rect1<rect2:
    print("The area of the first rectangle is lesser than the second one.")
else:
    print("The area of the second rectangle is lesser than the first one.")
