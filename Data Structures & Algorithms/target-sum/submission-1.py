class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0 
        for i  in nums:
            total += i
        
        if  (total + target)%2 != 0:
            return 0
        
        targetSum = (total + target)//2
        dp = [[-1]*(targetSum+1) for _ in range(len(nums)+1)]
        # nums.sort()
        def solve(i, targetSum):
            # if targetSum == 0:
            #     return 1
            
            if i >= len(nums):
                return 1 if targetSum == 0 else 0
            
            if dp[i][targetSum] != -1:
                return dp[i][targetSum]

            # take
            ans1, ans2 = 0 , 0 
            if nums[i] <= targetSum :
                ans1 = solve(i+1, targetSum - nums[i])
                
            # not take 
            ans2 = solve(i+1, targetSum )

            dp[i][targetSum] = ans1 + ans2 
            return ans1 + ans2 

        return solve(0, targetSum)