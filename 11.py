a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
def gcd(a,b):
    if(a<b):
        a,b=b,a
    else:
        r=a%b
        if(r==0):
            return b
        else:
            while(r!=0):
                a=b
                b=r
                r=a%b
            return b
print("The GCD of the two numbers is:",gcd(a,b))            
