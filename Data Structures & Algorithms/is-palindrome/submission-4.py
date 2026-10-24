class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for ch in s:
            if ch.isalnum():
                temp.append(ch.lower())

        i,j = 0, len(temp)-1
        # print(temp)
        while i < j:
            if temp[i]!=temp[j]:
                return False
            i,j = i+1,j-1
        
        return True
