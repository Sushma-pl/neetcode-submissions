class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*(n)

        def dfs(i, parent):
            visited[i] = True
            
            for u in adj[i]:
                if not visited[u]:
                    if(dfs(u, i)):
                        return True
                elif visited[u] and parent != u:
                    return True
            
            return False

        # connected
        if dfs(0,-1):
            return False

        
        for i in range(n):
            if not visited[i] :
                    return False
        
        return True