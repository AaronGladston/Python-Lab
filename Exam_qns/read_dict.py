import csv
with open("names.csv","r") as file:
    nyfile = csv.reader(file)
    keys = []
    values = []
    for row in nyfile:
        for i in row:
            keys.append(i)
            values.append(len(str(i)))
keys.sort()
dict1 = {keys[i]:values[i] for i in range(len(keys))}
with open("dict.csv","w",newline='') as csvfiel:
    writer = csv.writer(csvfile)
    for key in dict1:
        writer.writerow([key,dict1[key]])