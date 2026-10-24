# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        
        # maxp  = float('inf')
        minp = float('-inf')

        def solve(root, minp):
            if root is None:
                return 
            
            if root.val >= minp:
                self.count += 1
                minp = root.val
            
            solve(root.left, minp)
            solve(root.right, minp)
            
        
        solve(root,minp)
        return self.count
        
                