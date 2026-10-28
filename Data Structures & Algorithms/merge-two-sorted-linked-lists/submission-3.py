# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # assing a dummy node 
        # node = ListNode(0)
        # dummy = node

        def solve(l1, l2):
            if l1 is None:
                return l2
            
            if l2 is None:
                return l1

            if l1.val <= l2.val:
                temp = l1
                temp.next = solve(l1.next, l2)
            else:
                temp = l2
                temp.next = solve(l1, l2.next)
            
            return temp

        return solve(list1,list2)
        # return dummy.next 

        