class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:    
        def setrowzero(i):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
        
        def setcolzero(j):
            for i in range(len(matrix)):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
        
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        setrowzero(i)
                        setcolzero(j)

        print(matrix)
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == float('inf'):
                         matrix[i][j] = 0
        