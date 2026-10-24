class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs 
        m, n = len(grid), len(grid[0])
        direction = [[0,-1], [1,0], [0,1], [-1,0]]
    
        # multi source bfs
        visited = [[False]*n for _ in range(m)]
        q = deque()

        # append all gate in the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited[i][j] = True
                    q.append((i,j,0))

        while q:
            size = len(q)

            for i in range(size):
                x,y,d = q.popleft()

                for x1, y1 in direction:
                    r, c = x + x1, y + y1
                    isValid = r>=0 and c >= 0 and r < m and c < n
                    if isValid and not visited[r][c] and grid[r][c] == 2147483647:
                        q.append((r,c,d+1))
                        visited[r][c] = True
                        grid[r][c] = d+1
        
            

            
