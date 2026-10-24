class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}

        if len(s1) > len(s2):
            return False
        
        for ch in s1:
            d1[ch] = 1 + d1.get(ch,0)
        
        l , k = 0 , len(s1)

        for r in range(len(s2)):
            if s2[r] in d1:
                d1[s2[r]] = d1[s2[r]]-1
            else:
                l = r+1
            
            if r-l+1 == k:  
                if max(d1.values()) == 0:
                    return True
                else:
                    d1[s2[l]] = d1[s2[l]]+1
                    l+=1
                   
                        
        return False