class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = []

        for i in range(len(temperatures) - 1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            
            # print(st)
            
            if not st :
                ans.append(0)  
            else:
                ans.append(st[-1]-i)

            # print(ans)
            st.append(i)
        
        return ans[::-1]