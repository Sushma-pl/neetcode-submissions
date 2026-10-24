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
            ltree = self.solve(root.left,d)
            rtree = self.solve(root.right,d)
            diameter =  ltree + rtree

            d[root] = max(ltree ,rtree ) + 1
            self.ans = max(self.ans, diameter)

        return d[root]
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        self.ans = 0

        temp = self.solve(root, d)
        return self.ans

        # q = deque()
        # q.append(root)

        # while q:
        #     root = q.popleft()
        #     diameter = d.get(root.left,0) + d.get(root.right,0)
        #     ans = max(ans, diameter)
            
        #     if root.left:
        #         q.append(root.left)
            
        #     if root.right:
        #         q.append(root.right)
        
        return self.ans

            

