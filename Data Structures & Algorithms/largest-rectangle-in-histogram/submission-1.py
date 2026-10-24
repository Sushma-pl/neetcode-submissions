class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # minimum to the right
        # minr = []
        # minl = []
        width = []
        st = []

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
                # minl.append(st[-1])
                width[i] = width[i] - st[-1] -1
            # else:
            #     # minl.append(-1)
            #     width[i] = width[i] 
            
            st.append(i)

        ans = 0 
        

        for i in range(len(heights)):
            # ans = max(ans, (minr[i]-minl[i]-1)*heights[i])
            ans = max(ans, (width[i])*heights[i])

        
        return ans 