# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root: Optional[TreeNode], d) -> int:
        if root is None:
            return 0

        if root not in d:
            d[root] = max(self.solve(root.left,d) , self.solve(root.right,d))+1

        return d[root]
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        self.solve(root, d)

        q = deque()
        q.append(root)

        ans = 0 
        while q:
            root = q.popleft()
            diameter = d.get(root.left,0) + d.get(root.right,0)
            ans = max(ans, diameter)
            
            if root.left:
                q.append(root.left)
            
            if root.right:
                q.append(root.right)
        
        return ans

            

