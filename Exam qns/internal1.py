class Location:
    def __init__(self, row, column):
        if row <= 0 or column <= 0:
            raise ValueError("Row and column values must be positive integers")
        self.r = row
        self.c = column
        self.matrix = self.read_values()

    def read_values(self):
        matrix = []
        for i in range(self.r):
            row = [int(input(f"A[{i},{j}]: ")) for j in range(self.c)]
            matrix.append(row)
        return matrix

    def display(self):
        print("\nMatrix:")
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def max_value(self):
        max_val = max(max(row) for row in self.matrix)
        print(f"Maximum value: {max_val}")

    def max_ind(self):
        maxm = self.matrix[0][0]
        ind = (0, 0)
        for i in range(self.r):
            for j in range(self.c):
                if maxm < self.matrix[i][j]:
                    maxm = self.matrix[i][j]
                    ind = (i + 1, j + 1)
        print("Index:", ind)

    def transpose(self):
        self.transpose = [[self.matrix[j][i] for j in range(self.r)] for i in range(self.c)]

    def dis_trans(self):
        print("Transpose matrix:")
        for row in self.transpose:
            print(" ".join(map(str, row)))

row_1 = int(input("Enter the number of rows: "))
column_1 = int(input("Enter the number of columns: "))
obj_1 = Location(row_1,column_1)
obj_1.display()
obj_1.max_value()
obj_1.max_ind()
obj_1.transpose()
obj_1.dis_trans()