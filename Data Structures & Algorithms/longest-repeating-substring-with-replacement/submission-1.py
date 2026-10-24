class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        ans = 1
        maxcount = 0 
        l = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            maxcount = max(d.values())
            
            # check whether window is valid or not 
            while r-l+1 - maxcount > k:
                d[s[l]] = d[s[l]] - 1
                l += 1
                maxcount = max(d.values())

            ans = max(ans, r-l+1)
        
        return ans 
