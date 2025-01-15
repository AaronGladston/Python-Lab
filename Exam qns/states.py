import csv

n = int(input("Enter the number of state names: "))
keys = [input("Enter the state names:\n") for i in range(n)]
values = [len(str(word)) for word in keys]
dict1 = {keys[i]:values[i] for i in range(n)}
keys.sort()
dict2 = {i:dict1[i] for i in keys   }

with open("34_new.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    for key in dict2:
        writer.writerow([key,dict2[key]])

with open("34_new.csv","r") as myfile:
    csvf = csv.reader(myfile)
    for row in csvf:
        print(row)  