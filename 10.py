from math import sqrt
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a==0):
    print("This is not a quadratic equation.")
else:
    d=b*b-(4*a*c)
    if(d==0):
        print("The root of the quadratic equation is:",(-b)/(2*a))
    elif(d>0):
        root1=((-b)+sqrt(d))/(2*a)
        root2=((-b)-sqrt(d))/(2*a)
        print("The first root of the quadratic equation is:",root1,"and the second root is:",root2)
    else:
        root1=(-b)/(2*a)
        root2=sqrt(-d)/(2*a)
        print("The first root of the quadratic equation is:",root1,"+i",root2,"and the second root is:",root1,"-i",root2)
