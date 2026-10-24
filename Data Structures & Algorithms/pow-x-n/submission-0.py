class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = abs(n)
        temp = 1
        while p != 0:
            temp = temp*x
            p -= 1
        
        if n > 0 :
            return temp
        else:
            return 1/temp