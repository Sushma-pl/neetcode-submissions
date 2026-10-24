class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 ,len(nums)-1
        while l <= r :
            m = (l+r)//2

            if nums[m] == target:
                return m
            
            # left sorted array
            if nums[l] <= nums[m]:
                if nums[m] < target  or  target < nums[l]:
                    l = m+1
                else: # nums[m] > target:
                    r = m-1
                    # elif target < nums[l]:
                    #     l = m+1 

            else: #right sorted array
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1 
        
        return -1

