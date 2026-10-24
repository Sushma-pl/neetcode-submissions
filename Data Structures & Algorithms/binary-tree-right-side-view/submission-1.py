# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root is None:
            return ans
        
        q  = deque()
        q.append(root)
        
        while q:
            qlen = len(q)
            rightValue = -101
            for i in range(qlen):
                temp =  q.popleft()
                rightValue = temp.val

                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
            ans.append(rightValue)
        return ans 
        

