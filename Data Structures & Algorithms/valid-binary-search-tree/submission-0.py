# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxp = float('inf')
        minp = float('-inf')

        def solve(root, maxp, minp):
            if root is None:
                return True
            else:
                cond1 =  (root.val > minp and root.val < maxp)
                cond2 = solve(root.left, root.val , minp)
                cond3 = solve(root.right, maxp, root.val)
                return cond1 and cond2 and cond3 
        
        return solve(root, maxp, minp)