class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for f, t in tickets:
            adj[f].append(t)
        
        for k in adj.keys():
            adj[k].sort()

        ans = []
        

        def dfs(location):
            if len(ans) == len(tickets)+1:
                return True
            if location not in adj:
                return False

            temp = list(adj[location])

            for i,t in enumerate(temp):
                adj[location].pop(i)
                ans.append(t)

                if dfs(t): return True

                # bvacktrack
                ans.pop()
                adj[location].insert(i, t)

            return False




        ans.append("JFK")
        dfs("JFK")
        print(ans)
        return ans
