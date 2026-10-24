class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # myset = set(nums) #O(n)
        nums.sort()
        c = 0
        ans = 0
        lastseen = -sys.maxsize
        for i in range(len(nums)):
            if nums[i] == lastseen:
                continue 

            if lastseen == -sys.maxsize or nums[i] == lastseen+1:
                c+=1
            else:
                c = 1
            lastseen = nums[i]
            
            ans = max(c, ans)

        return ans 