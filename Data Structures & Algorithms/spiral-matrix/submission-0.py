class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        c = len(matrix[0]) - 1
        r = len(matrix) - 1
        fr, fc, lr, lc = 0,0, r , c
        ans  = []
        while fr <= lr and fc <= lc:
            # first row
            if fr <= lr and fc <= lc:
                for i in range(fc, lc+1):
                    ans.append(matrix[fr][i])
                fr += 1
            
            if fr <= lr and fc <= lc:
                for i in range(fr,lr+1):
                    ans.append(matrix[i][lc])
                lc -= 1
            
            if fr <= lr and fc <= lc:
                for i in range(lc, fc-1, -1):
                    ans.append(matrix[lr][i])
                lr -= 1

            if fr <= lr and fc <= lc:
                for i in range(lr, fr-1, -1):
                    ans.append(matrix[i][fc])
                fc += 1
                
        return ans