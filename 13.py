def fact(x):
    if(x==0) or (x==1):
        return 1
    else:
        f=1
        while(x>0):
            f=f*x
            x-=1
        return f
x=int(input("Enter the number:"))
print("The factorial of",x,"is:",fact(x))
