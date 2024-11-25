dict={}
key=[]
values=[]
n=int(input("Enter the number of enteries to be made in the dictionary:\n"))
print("Input the keys of the dictionary")
for i in range(n):
    key.append(int(input()))
print("Input the corresponding values of keys")
for i in range(n):
    values.append(input())
dict={key[i]:values[i] for i in range(n)}
print(dict)
key.sort()
for i in range(n):
    

    







