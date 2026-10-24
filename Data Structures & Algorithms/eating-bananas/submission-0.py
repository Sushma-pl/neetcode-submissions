class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        ans = float('inf') 

        l , r = 1, piles[n-1]
        while l <= r:
            m = (l+r)//2

            if self.solve(piles, h, m) <= h:
                ans = min(ans, m)
                r = m-1
            else:
                l = m+1 
        
        return ans 

    def solve(self,piles :List[int], h : int, k :int)->int:
        count = 0 
        for n in piles:
            count += n//k 
            count += 1 if n%k != 0 else 0
        # print(k, count)
        return count 
