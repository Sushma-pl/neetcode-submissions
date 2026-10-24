class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        # print(nums)
        for i in range(len(nums)):
            target = -nums[i]
            j,k = i+1, len(nums)-1
            # print(i,j,k, ans)
            while j < k:
                if nums[j]+nums[k] == target:
                    ans.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    j+=1
                

        return list(list(item) for item in ans )