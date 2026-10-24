class Solution:
    def squares(self, n):
        temp = 0
        while n != 0:
            temp += (n%10)*(n%10)
            n = n//10
        
        return temp

    def isHappy(self, n: int) -> bool:
        slow, fast = n , self.squares(n)

        while slow != fast:
            fast = self.squares(fast)
            fast = self.squares(fast)
            slow = self.squares(slow)
        
        return True if fast==1 else False
