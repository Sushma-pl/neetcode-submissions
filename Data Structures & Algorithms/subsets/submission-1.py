class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    # solve using recusion
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = []
        inp = nums
        ans = []

        def solve(inp, op , i):
            if i == len(inp):
                ans.append(op)
                return

            # Take    
            op1 = op.copy()
            op1.append(inp[i])
            solve(inp,op1,i+1)
           
           
            # Not take 
            op2 = op.copy() 
            solve(inp,op2,i+1) 

        solve(inp,op,0)
        return ans  