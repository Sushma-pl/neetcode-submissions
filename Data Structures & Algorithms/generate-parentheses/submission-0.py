class Solution:
    def solve(self, o:int, c:int, s: str):
        if o == 0 and  c == 0:
            self.ans.append(s)
        elif  o < c :
            if c >0 :
                self.solve(o,c-1,s+")")
            if o > 0:
                self.solve(o-1,c,s+"(")
        elif o >= c:
                self.solve(o-1,c,s+"(")



    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        s = "("
        self.solve(n-1,n,s)
        return self.ans