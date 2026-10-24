class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*(n)

        q = deque()
        q.append((0,-1))
        visited[0] = True

        while q:
            x, p = q.popleft()

            for u in adj[x]:
                if not visited[u]:
                    q.append((u,x))
                    visited[u] = True
                elif visited[u] and p != u:
                    return False
                    # not a tree, forming cycle
        
        for i in range(n):
            if not visited[i]:
                return False
                # not all node connected
    
        return True