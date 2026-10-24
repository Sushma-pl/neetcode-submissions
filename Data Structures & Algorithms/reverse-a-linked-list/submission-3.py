# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            # it should return last node whole next is none, but we need head also
            if node and node.next:
                newhead, tail = helper(node.next)
                tail.next = node
                node.next = None
                return [newhead, node]
            else:
                return [node, node]
        newhead, _ = helper(head)
        return newhead