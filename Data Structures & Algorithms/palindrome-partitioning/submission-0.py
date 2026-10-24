class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPallindrome(i,j):
            while i <= j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True

        def solve(i, j, out):
            if i > j:
                ans.append(out.split('#')[1:])
                return
            
            for k in range(i, j+1):
                if isPallindrome(i, k):
                    solve(k+1, j, out + "#" + s[i:k+1])
        
        solve(0, len(s)-1, "")
        return ans
