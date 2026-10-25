class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l,r =0, n-1
        while l <=r:
            m = (l+r)//2

            if arr[m]==target:
                return m
            elif arr[l] <= arr[m]:
                if target >= arr[l] and target <= arr[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if target >= arr[m] and target <= arr[r]:
                    l = m+1
                else:
                    r = m-1
        
        return -1
