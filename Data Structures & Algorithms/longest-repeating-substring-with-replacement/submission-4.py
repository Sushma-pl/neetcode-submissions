class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        d = [0]*26
        i,j = 0,0
        while j < n:
            d[ord(s[j])-ord('A')]+= 1
            maxc = max(d)
            length = j-i+1

            if length - maxc <= k:
                ans = max(length, ans)
            else:
                if length - maxc > k:
                    d[ord(s[i])-ord('A')]-= 1
                    maxc = max(d)
                    i+=1
                    length = j-i+1

            j+=1

        return ans 


