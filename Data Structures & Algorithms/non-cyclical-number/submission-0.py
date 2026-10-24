class Solution:
    def isHappy(self, n: int) -> bool:
        myset = set()
        myset.add(n)

        while n != 1:
            temp = 0
            while n != 0:
                temp += (n%10)*(n%10)
                n = n//10
            n = temp 
            if n in myset:
                return False
            myset.add(n)
        
        return True
