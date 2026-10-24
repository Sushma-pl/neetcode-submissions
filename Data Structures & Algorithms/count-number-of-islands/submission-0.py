class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        dr = [1,0,-1,0]
        dc = [0,1,0,-1]

        def solve(r,c, rows,cols):
            q = deque()
            q.append((r,c))
            while q:
                x, y = q.popleft()
                
                for i in range(4):
                    newr = x + dr[i]
                    newc = y + dc[i]
                    if newr >= 0 and newr < rows and newc >= 0 and newc < cols and not visited[newr][newc] and grid[newr][newc] == '1':
                        visited[newr][newc] = 1
                        q.append((newr, newc))
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    count += 1
                    visited[i][j]=1
                    solve(i,j, rows, cols)
            


        return count 








