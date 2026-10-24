# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def height(self, root:Optional[TreeNode])->int:
    #     if root is None:
    #         return 0
        
    #     return max(self.height(root.left), self.height(root.right)) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        d = {}


        def solve(root, d):
            if root is None:
                return True, 0
                
            if root.left in d:
                lb , lh = d[root.left]
            else:
                lb , lh = solve(root.left, d)

            if root.right in d:
                rb , rh = d[root.right]
            else:
                rb , rh = solve(root.right, d)
            
            isbalance = abs(lh-rh) <= 1 and lb and rb
            height = max(lh,rh) +1 
            return isbalance, height
            
        isbalance, height = solve(root,d)
        return isbalance

