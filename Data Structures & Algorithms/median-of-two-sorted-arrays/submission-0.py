class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        # I want nums1 to be 
        if n1 <=  n2:
            small = nums1
            large = nums2
        else:
            small = nums2
            large = nums1

        

        l, r = 0, len(small)-1
        # l2, r2 = 0, len(large)-1
        
        
        half = (n1+n2)//2  
        
        while True:
            m = (l+r)//2
            # print(l,r, m)


            rem = half-(m+1) - 1 #index
            small_left = small[m] if m >= 0  else float('-inf')
            small_right =  small[m+1] if (m+1) < len(small) else float('inf')

            # print(small_left, small_right)

            large_left = large[rem] if rem >= 0 else float('-inf')
            large_right = large[rem+1] if rem+1 < len(large) else float('inf')
            # print(large_left, large_right)

            if small_left <= large_right and large_left <= small_right:
                # calculate median
                if (len(small) + len(large))%2 == 0:
                    return (max(small_left,large_left) + min(small_right, large_right))/2
                else:
                    return min(small_right, large_right)
            elif small_left > large_right:
                r = m-1
            else:
                l = m+1 
        
            
        return -1

