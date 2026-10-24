class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        for word in strs:
            l  = len(word)
            temp.append(str(l)+";")
            temp.append(word)
        
        return "".join(temp)


    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        ans = []

        while i < n:
            l = i
            
            # find length
            while i < n and s[i]!=';':
                i+=1
            length = int(s[l:i])
            i+=1

            # find string
            temp = s[i:i+length]
            ans.append(temp)
            i = i+length
        return ans 

