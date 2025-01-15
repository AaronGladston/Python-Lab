class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0]) if matrix else 0 
    def transpose(self):
        transposed = [[self.matrix[j][i] for j in range(self.rows)]for i in range(self.columns)]
        return Matrix(transposed)   
    def check_matrix_type(self):
        is_upper = True
        is_lower = True
        is_diagonal = True
        
        for i in range(self.rows):
            for j in range(self.columns):
                if i>j and self.matrix[i][j]!=0:
                    is_upper = False
                if i<j and self.matrix[i][j]!=0:
                    is_lower = False
                if i!=j and self.matrix[i][j]!=0:
                    is_diagonal = False
        if is_diagonal:
            return f"Diagonal matrix."
        elif is_lower:
            return f"Lower triangular matrix."
        elif is_upper:
            return f"Upper triangular matrix."
        else:
            return f"Neither upper triangular, lower triangular nor diagonal matrix."
    def find_smallest_element(self):
        mini = float('inf')
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j]<mini:
                    mini = self.matrix[i][j]
                    u = i
                    v = j
        return mini,u,v
    def __str__(self):
        return f"\n".join(["\t".join(map(str,row))for row in self.matrix])
if __name__=='__main__':
    matrix_data = [
        [1,2,3],
        [0,5,6],
        [0,0,9]
    ]
    matrix = Matrix(matrix_data)
    print("Original Matrix:")
    print(matrix)
    print("\nTranspose of the Matrix:")
    print(matrix.transpose())
    print("\nMatrix Type:")
    print(matrix.check_matrix_type())
    mini, u, v = matrix.find_smallest_element()
    print("\nSmallest Element:",mini,"Index:",u,v)