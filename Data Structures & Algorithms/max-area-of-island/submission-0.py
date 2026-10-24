class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        
        dr = [1,0,-1,0]
        dc = [0,1,0,-1]
        
        ans = 0

        def solve(r,c):
            q = deque()
            island_area = 1
            q.append((r,c))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    newr = x + dr[i]
                    newc = y + dc[i]
                    if newr >= 0 and newr < rows and newc >= 0 and newc < cols and (not visited[newr][newc]) and grid[newr][newc]:
                        visited[newr][newc] = 1
                        island_area += 1
                        q.append((newr, newc))
            return island_area
        
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j]:
                    visited[i][j]=1
                    ans = max(ans, solve(i,j))
                    
            
        return ans