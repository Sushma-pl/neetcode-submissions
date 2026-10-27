class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = Counter(t)
        d ={}
        n = len(s)
        ans = ""
        l,r =-100000,100000
        i,j =0,0
        count =0
        while j < n:
            # we will always get the shprtedt length
            while i <= j and s[i] not in tfreq :
                i+=1

            while i <=j and s[i] in d and d[s[i]] > tfreq[s[i]]:
                d[s[i]]-=1
                i+=1

            if s[j] in tfreq:
                d[s[j]] = d.get(s[j], 0) + 1
                # first time it become equal
                if d[s[j]] == tfreq[s[j]]:
                    count += 1

            if count == len(tfreq):
                if (r-l+1) > (j-i+1):
                    l,r =i,j

                # slide window by one time
                if s[i] in d:
                    d[s[i]]-=1
                    if d[s[i]] < tfreq[s[i]]:
                        count -= 1
                i+=1
            
            j+=1
            
        ans = s[l:r+1] if l!= -100000 else ""   
        return ans
