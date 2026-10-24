class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        

        for i in range(len(matrix)):
            if i not in row:
                continue
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            if j not in col:
                continue
            for i in range(len(matrix)):
                matrix[i][j] = 0
    

        