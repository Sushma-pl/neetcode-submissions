class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if maxReach >= i:
                maxReach = max(maxReach, i+nums[i])
            else:
                return False
            
        return maxReach >= (len(nums)-1)