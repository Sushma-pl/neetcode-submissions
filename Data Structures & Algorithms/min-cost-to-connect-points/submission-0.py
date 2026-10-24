class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
       min_heap = []
       ans = 0
       visited = set()
       heapq.heappush(min_heap, (0, points[0][0], points[0][1])) 
       
       while min_heap:
            d, x, y = heapq.heappop(min_heap)
            
            if (x,y) not in visited:
                visited.add((x,y))
                ans += d

                for x1, y1 in points:
                    if (x,y) != (x1,y1) and (x1,y1) not in visited:
                        manhd = abs(x-x1) + abs(y-y1)
                        heapq.heappush(min_heap, (manhd, x1,y1))
            
       return ans
         