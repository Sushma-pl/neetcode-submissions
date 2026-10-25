class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1 or  nums[0]< nums[n-1]:
            return nums[0]
        
        l,r = 0, n-1

        while l <= r:
            m = (l+r)//2

            p = nums[(m-1+n)%n]
            ne = nums[(m+1)%n]

            if nums[m] < p and nums[m] < ne:
                return nums[m]
            else:
                if nums[m] >= nums[0]:
                    l = m+1
                else:
                    r = m-1
        
        return -1
        
