# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        d = {}

        q = deque()
        q.append((root, 1))
        while q:
            node, level = q.popleft()
            if level in d:
                d[level].append(node.val)
            else:
                d[level] = [node.val]

            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1 ))
        
        ans = []
        for k in d.keys():
            ans.append(d[k])

        return ans
