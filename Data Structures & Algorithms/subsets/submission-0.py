class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        inp = nums
        op = []

        def backtrak(inp, op, i):
            ans.append(op)
            
            if i == len(inp):
                return 
                
            j = i 
            # newop = op.copy()

            while j < len(inp):
                op.append(inp[j])
                backtrak(inp, op.copy(), j+1 )
                op.pop()
                j += 1
        
        backtrak(inp,op,0)
        return ans