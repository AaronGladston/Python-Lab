c=0
while(c<5):
    print("This is a menu-driven calculator for performing arithmetic operations.\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
    c=int(input("Enter your choice number:"))
    a=int(input("Enter the number for operation:"))
    b=int(input("Enter the number for operation:"))
    if(c==1):
       print("The sum of the two numbers is= ",a+b)
    elif(c==2):
       print("The difference of the two numbers is= ",a-b)
    elif(c==3):
       print("The product of the two numbers is= ",a*b)
    elif(c==4):
       print("The quotient of the two numbers is= ",a/b)
    else:
       print("Please enter a valid choice.")
       break
    
