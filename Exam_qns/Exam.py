m =[
    [1,2,3]
    [3,4,5]
]
for i in range(2):
    for j in range(3):
        m[i][j] = m[j][i]
        print(m[j][i],"\t")
    print("\n") 