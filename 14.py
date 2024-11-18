def fib(n):
    a,b,list1=-1,1,[]
    while(n>0):
        c=a+b
        a=b
        b=c
        n-=1
        list1.append(c)
    return list1
n=int(input("Enter the limit:"))
print("The fibonacci series upto",n,"terms is:",fib(n))
