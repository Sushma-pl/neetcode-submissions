class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums) #O(n)

        c = 0
        for key in myset:
            temp= 1
            n = key
            if n-1 not in myset:
                while n+1 in myset:
                    temp += 1
                    n += 1
            c = max(c, temp)

        return c
     
