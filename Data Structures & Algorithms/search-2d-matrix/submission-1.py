class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = -1

        l = 0 
        r = len(matrix)-1
        c = len(matrix[0])-1

        while l <= r:
            m = (l+r)//2

            if target >= matrix[m][0]  and target <= matrix[m][c]:
                index = m 
                break 
            elif target >= matrix[m][0]:
                l +=  1
            else:
                r -= 1
        
        if index == -1:
            return False
        
        l , r = 0 , c

        while l <= r:
            m = (l+r)//2

            if target == matrix[index][m]:
                return True
            elif target > matrix[index][m]:
                l += 1
            else:
                r -= 1


        return False