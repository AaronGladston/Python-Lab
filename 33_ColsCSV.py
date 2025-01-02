import csv
with open("33_file.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    file = next(reader)
    n = int(input("Enter the specific columns of your choice: "))
    col = []
    for row in reader:
        col.append(row[n])
    print(file[n],"\n",col)
