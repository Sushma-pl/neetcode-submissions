class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in closeToOpen:
                if st and st[-1] == closeToOpen[i]:
                    st.pop()
                else: 
                    return False
            else:
                st.append(i)
        
        if st:
            return False

        return True
                

