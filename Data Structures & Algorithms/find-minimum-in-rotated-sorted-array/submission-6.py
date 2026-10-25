class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        l,r =0 , n-1
        while l < r :
            m = (l+r)//2

            if arr[m] > arr[r]:
                l = m+1
            else:
                r = m
        return arr[l]