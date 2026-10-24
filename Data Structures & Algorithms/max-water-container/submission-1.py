class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        ans = 0
        while i < j:
            l = j-i
            h = min(heights[i], heights[j])
            ans = max(ans, h*l)

            if heights[i]> heights[j]:
                j-=1
            else:
                i+=1
        
        return ans 