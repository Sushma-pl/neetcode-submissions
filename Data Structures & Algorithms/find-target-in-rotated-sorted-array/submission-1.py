class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
        res = nums[0]
        index = 0

        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < res:
                    res, index = nums[l], l
                break

            m = (l+r)//2
            
            if nums[m] < res:
                res, index = nums[l], m
            
            
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        
        return index

    def bsearch(self, nums: List[int], target: int, l: int,r: int) -> int:
        while l <=  r:
            m = (l+r)//2

            if nums[m] == target:
                return m 
            elif nums[m] < target:
                l = m+1
            else :
                r = m-1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums)-1
        mid = self.findMinIndex(nums)
        ans = self.bsearch(nums, target, l, mid-1)
        # print(mid)
        if ans != -1:
            return ans
        else :
            return self.bsearch(nums, target, mid, r)

