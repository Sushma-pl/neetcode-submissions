# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # self.count = 0
        
        # maxp  = float('inf')
        minp = float('-inf')

        def solve(root, minp):
            if root is None:
                return 0
            
            if root.val >= minp:
                minp = root.val
                # self.count += 1
                return 1 + solve(root.left, minp) + solve(root.right, minp)
            else:
                return solve(root.left, minp) + solve(root.right, minp)
            
        
        return solve(root,minp)
        # return self.count
        
                