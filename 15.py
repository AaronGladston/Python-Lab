a=input("Enter the string:").lower()
b=set(a)
for j in b:
    c=0
    for i in a:
        if i is j:
            c+=1
    print("The frequency of the charcter",j,"is:",c)

