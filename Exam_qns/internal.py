class Location:
    def __init__(self,row,column):
        self.r=row
        self.c=column
        self.matrix=self.read_values()
    def read_values(self):
        matrix=[]
        for i in range(self.r):
            row=[]
            for j in range(self.c):
                value=int(input(f"A[{i},{j}]:"))
                row.append(value)
            matrix.append(row)
        return matrix

    def display(self):
        print("\nMatrix")
        for i in range(self.r):
            for j in range(self.c):
                print(self.matrix[i][j],end=" ")
            print()
            
    def max_value(self):
        a=max(self.matrix)
        b=max(a)
        print(f"Maximum value {b}")
        
        
    def max_ind(self):
        maxm=self.matrix[0][0]
        for i in range(self.r):
            for j in range(self.c):
                if(maxm<self.matrix[i][j]):
                    maxm=self.matrix[i][j]
                    ind=(i+1,j+1)
        
        # print("Max value :",maxm)
        print("Index :",ind)
    
    def transpose(self):
        self.transpose=[]
        for i in range(self.r):
            t=[]
            for j in range(self.c):
                value=self.matrix[j][i]
                t.append(value)
            self.transpose.append(t)


    def dis_trans(self):
        print("Transpose matrix")
        for i in range(self.r):
            for j in range(self.c):
                print(self.transpose[i][j],end=" ")
            print("")
        print(self.transpose)

        
obj_1=Location(2,2)
obj_1.display()
obj_1.max_value()
obj_1.max_ind()
obj_1.transpose()
obj_1.dis_trans()