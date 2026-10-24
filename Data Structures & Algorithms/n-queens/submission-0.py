class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.']*n for _ in range(n)]
        # print(board)
        def isPossible(row,col):
            # row
            for i in range(0,n):
                # print(i,col)
                if board[i][col] == 'Q':
                    return False
            
            for j in range(0,n):
                # print("col", row, j)
                if board[row][j] == 'Q':
                    return False
            
            for i in range(1, n):
                if row+i < n and col+i < n and board[i+row][i + col] == 'Q':
                    return False
                if row-i >= 0 and col-i >= 0 and board[row-i][col-i] == 'Q':
                    return False
            
            for i in range(1, n):
                if row-i >= 0 and col+i < n and board[row-i][i + col] == 'Q':
                    return False
                if row+i < n and col-i >= 0 and board[row+i][col-i] == 'Q':
                    return False
            
            return True
                

        def solve(col):
            # print("solve(" , col ," ) called")
            
            if col >= n:
                temp = []
                for i in range(0,n):
                    temp.append("".join(board[i]))
                # print(temp)
                ans.append(temp)
                return 
            

            for i in range(0,n):
                if isPossible(i, col):
                    board[i][col] = 'Q'
                    solve(col+1)
                    board[i][col] = '.'
        
        solve(0)
        # isPossible(0,0)
        return ans


