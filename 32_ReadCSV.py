import csv
file = open("32_name.csv","r")
reader = csv.reader(file)
for row in reader:
    print(row)