l1 = list(map(int,input("Enter the list:\n").split()))
new_list = [i for i in l1 if i % 2 != 0]
print("The list with no even numbers is as follows:\n", new_list)
