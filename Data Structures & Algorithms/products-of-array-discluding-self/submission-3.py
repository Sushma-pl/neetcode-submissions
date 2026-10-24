class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p, n = [1]*len(nums),[1]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                p[i] = (nums[i])
            else:
                p[i] = (p[i-1]*nums[i])

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                n[i] = (nums[i])
            else:
                n[i] = n[i+1]*nums[i]
        
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(n[i+1])
            elif i == len(nums)-1:
                ans.append(p[i-1])
            else:
                ans.append(p[i-1]*n[i+1])
        return ans