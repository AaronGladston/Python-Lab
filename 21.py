dict={}
key=[]
values=[]
n=int(input("Enter the number of enteries to be made in the dictionary:\n"))
print("Input the keys of the dictionary")
for i in range(n):
    key.append(int(input()))
print("Input the values of the corresponding keys")
for i in range(n):
    values.append(input())
dict={key[i]:values[i] for i in range(n)}
print("Initial dictionary:",dict)
keys=list(dict.keys())
keys.sort()
print("The dictionary sorted in ascending order is:")
for k in keys:
    print(f"{k}: \'{dict[k]}\'",end=",")
print("\n")
print("The dictionary sorted in descending order is:")
keys.reverse()
for k in keys:
    print(f"{k}: \'{dict[k]}\'",end=",")







    
