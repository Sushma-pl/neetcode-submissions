class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right =0,0
        n = len(s)
        lastSeen = {}
        ans = 0
        while right < n:
            if s[right] in lastSeen:
                left = max(left, lastSeen[s[right]]+1)
            
            lastSeen[s[right]] = right
            ans = max(ans, right-left+1)
            right +=1 
        
        return ans