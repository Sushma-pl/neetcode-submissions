class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        max_freq = 0
        d = {}
        i,j = 0,0
        while j < n:
            d[s[j]]= d.get(s[j], 0) +1
            max_freq = max(max_freq, d[s[j]])
            length = j-i+1

            if length - max_freq <= k:
                ans = max(length, ans)
            else:
                d[s[i]]-= 1
                i+=1
            j+=1

        return ans 


