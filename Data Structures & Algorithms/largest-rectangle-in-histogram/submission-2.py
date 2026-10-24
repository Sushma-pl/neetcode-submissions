class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # minimum to the right
        width = []
        st = []
        ans = 0 
        
        for i in range(len(heights)-1, -1, -1):
            
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            
            if st:
                width.append(st[-1])
            else:
                width.append(len(heights))

            st.append(i)
        
        width.reverse()
        st.clear()

        for i in range(len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                width[i] = width[i] - st[-1] -1
            
            ans = max(ans, (width[i])*heights[i])
            st.append(i)

        
        

        # for i in range(len(heights)):
        #     ans = max(ans, (width[i])*heights[i])

        
        return ans 