class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap =  []
        for s in stones:
            maxheap.append(-1* s)

        # print(maxheap)
        heapq.heapify(maxheap)
        # print(maxheap)
        
        while len(maxheap) > 1:
            # print(maxheap[-1])
            first = -1* heapq.heappop(maxheap)
            second =  -1* heapq.heappop(maxheap)
            # print(first, second)
            
            if first - second > 0:
                heapq.heappush(maxheap, second-first)
        #     if abs(stone1-stone2) > 0:
        #         heapq.heappush(maxheap, -1* abs(stone1-stone2))

        return -1*maxheap[0] if maxheap else 0
        