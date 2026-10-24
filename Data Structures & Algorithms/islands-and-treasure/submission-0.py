class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs 
        m, n = len(grid), len(grid[0])
        direction = [[0,-1], [1,0], [0,1], [-1,0]]
    
        def bfs(i,j):
            visited = [[False]*n for _ in range(m)]
            visited[i][j] = True
            
            q = deque()
            q.append((i,j,0))

            while q:
                x,y,d = q.popleft()

                if grid[x][y] == 0:
                    grid[i][j] = d
                    break

                for x1, y1 in direction:
                    r, c = x + x1, y + y1
                    isValid = r>=0 and c >= 0 and r < m and c < n
                    if isValid and not visited[r][c] and grid[r][c] != -1:
                        q.append((r,c,d+1))
                        visited[r][c] = True
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2147483647:
                    bfs(i,j)
        
            

            
