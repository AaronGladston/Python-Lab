dict1={}
key=[]
values=[]
n=int(input("Enter the number of enteries to be made in the dictionary:\n"))
print("Input the keys of the dictionary")
for i in range(n):
    key.append(int(input()))
print("Input the values of the corresponding keys")
for i in range(n):
    values.append(input())
dict1={key[i]:values[i] for i in range(n)}
print("Initial dictionary:",dict1)
keys=list(dict1.keys())
keys.sort()
print("The dictionary sorted in ascending order is:")
ascending_dict = {k: dict1[k] for k in keys}
print(ascending_dict)
print("The dictionary sorted in descending order is:")
descending_dict = {k: dict1[k] for k in reversed(keys)}
print(descending_dict)






    
