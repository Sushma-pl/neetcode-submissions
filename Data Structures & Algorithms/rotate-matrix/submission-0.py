class Solution:
    def reverse(self, n, matrix):
        first , last = 0 ,n-1
        while(first <= last):
            for j in range(0,n):
                temp = matrix[first][j]
                matrix[first][j] = matrix[last][j]
                matrix[last][j] = temp
            
            first += 1
            last -= 1

    def transpose(self, n, matrix):
        for i in range(0,n):
            for j in range(i,n):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    
                    


    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        self.reverse(n, matrix)
        self.transpose(n, matrix)