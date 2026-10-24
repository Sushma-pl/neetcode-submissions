class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        ans = 0

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*(n)

        def dfs(i):
            visited[i] = True
            
            for u in adj[i]:
                if not visited[u]:
                    dfs(u)

        for i in range(n):
            if not visited[i] :
                ans += 1
                dfs(i)

        
        return ans