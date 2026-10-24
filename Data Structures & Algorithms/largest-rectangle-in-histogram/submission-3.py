class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # minimum to the right
        
        st = []
        ans = 0 


        for i,h in enumerate(heights):
            index = i
            while st and st[-1][1] > h:
                start , height = st.pop()
                ans = max(ans, (i-start)*height)
                index = start
            st.append([index,h])

        for i,h in st:
            ans = max(ans, (len(heights)-i)*h)

        return ans 