class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = []
        adj = defaultdict(list)

        for u,v,t in times:
            adj[u].append((v,t))

        visited = set()
        heapq.heappush(pq, (0,k)) 
        
        
        ans = float('-inf')

        while pq:
            t,u = heapq.heappop(pq)
            
            # print("pop: ", u, t)
            ans = max(ans, t)

            visited.add(u)
            
            # print(len(visited))
            
            if len(visited) == n:
                return ans 

            for v, t1 in adj[u]:
                if v not in visited:
                    heapq.heappush(pq, (t+t1, v))
        
        return -1
                

