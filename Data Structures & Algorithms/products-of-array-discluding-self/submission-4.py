class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        m = 1
        for i in range(len(nums)):
            ans.append(m)
            m *= nums[i]

        m= nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            ans[i]*=m
            m *=nums[i]
        
        return ans 
