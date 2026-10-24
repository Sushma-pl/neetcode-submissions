class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(k, i, j):
            if k >= len(word):
                return True
            
            if i < 0 or j >= len(board[0]) or i >= len(board) or j < 0:
                return False
            elif word[k] == board[i][j]  and not visited[i][j]:
                visited[i][j] = True
                ans1 = solve(k+1, i-1,j) or solve(k+1, i,j-1) or solve(k+1, i,j+1) or solve(k+1, i+1,j) 
                visited[i][j] = False
                return ans1
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[False]*len(board[0]) for _ in range(len(board))]

                if(solve(0,i,j)):
                    return True
        

        return False
            
            
            