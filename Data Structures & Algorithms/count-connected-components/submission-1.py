class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*(n)
        count = 0

        def bfs(i):
            q = deque()
            q.append(i)
            visited[i] = True
        
            while q:
                x = q.popleft()

                for u in adj[x]:
                    if not visited[u]:
                        q.append(u)
                        visited[u] = True
        
        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i)
                
    
        return count