class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i],i))
        
        arr.sort(key=lambda x:x[0])

        i, j = 0, len(nums)-1
        while i < j:
            temp = arr[i][0]+arr[j][0]
            if temp == target:
                return [arr[i][1], arr[j][1]] if arr[i][1] < arr[j][1] else [arr[j][1], arr[i][1]] 
            elif temp > target:
                j-=1
            else:
                i+=1
        return [-1,-1]