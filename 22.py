dict1,dict2={},{}
keys1,keys2=[],[]
values1,values2=[],[]
n1=int(input("Enter the number of enteries in the first dictionary:"))
n2=int(input("Enter the number of enteries in the second dictionary:"))
print("Enter the keys of the first dictionary:")
for i in range(n1):
    keys1.append(int(input()))
print("Enter the values of the corresponding keys:")
for i in range(n1):
    values1.append(input())
dict1={keys1[i]:values1[i] for i in range(n1)}
print("The first dictionary is:",dict1)
print("Enter the keys of the second dictionary:")
for i in range(n2):
    keys2.append(int(input()))
print("Enter the values of the corresponding keys:")
for i in range(n2):
    values2.append(input())
dict2={keys2[i]:values2[i] for i in range(n2)}
print("The second dictionary is:",dict2)



    
    
