class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        i = j = 0
        ans = []
        while j < len(nums):
            # calculation part for montonic queue, means remove element which are smaller than element at j
            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)
            
            while i > q[0]:
                q.popleft()
            
            # check window size 
            if j-i+1 == k:
                ans.append(nums[q[0]])
                i+=1
                j+=1
            else:
                j+=1

        return ans

        