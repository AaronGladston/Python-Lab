n=int(input("Enter the number:"))
x=int(input("Enter the number of multiples:"))
print("The multiples of the given number are:\n")
for i in range(1,x+1):
    print(n,"*",i,"=",n*i)
