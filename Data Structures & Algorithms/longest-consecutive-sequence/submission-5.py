class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        ans =0
        v = set(nums)
        for i in range(n):
            temp = nums[i]-1
            # start point
            if temp not in v:
                c = 0
                while temp+1 in v:
                    c+=1
                    temp+=1
                ans = max(ans, c)
        
        return ans