# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        n = p.val == q.val

        return l and r and n


    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if root is None and subroot is None:
            return True
        elif subroot is None:
            return True
        elif root is None:
            return False

        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            if temp.val == subroot.val:
                if self.isSameTree(temp, subroot):
                    return True

            if temp.left:
                q.append(temp.left)
            
            if temp.right:
                q.append(temp.right)
        
        return False
