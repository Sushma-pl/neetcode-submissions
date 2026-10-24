class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i]);
            elif st and st[-1] == '(' and s[i] == ')':
                st.pop()
            elif st and st[-1] == '{' and s[i] == '}':
                st.pop()
            elif st and st[-1] == '[' and s[i] == ']':
                st.pop()
            else:
                return False
        if st:
            return False
        return True;
                

