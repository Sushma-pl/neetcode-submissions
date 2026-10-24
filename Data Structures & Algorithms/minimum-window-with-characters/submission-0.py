class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d , d1= {}, {}
        ans = ""

        for ch in t:
            d[ch] = d.get(ch,0) + 1

        l = 0
        size = len(d)
        count = 0
        
        for r in range(len(s)):
            d1[s[r]] = d1.get(s[r],0) + 1
            
            if d1[s[r]] ==  d.get(s[r],0):
                count += 1

            if count == size:
                
                # find the correct starting point
                while s[l] not in d or d1[s[l]] > d.get(s[l],0):
                    d1[s[l]] = d1[s[l]] - 1
                    l += 1

                if len(ans) > r-l+1 or ans == "":
                    ans = s[l:r+1]
                
                # slide the window
                if s[l] in d:
                    d1[s[l]] =  d1[s[l]] - 1
                    count -= 1
                    l += 1

        return ans