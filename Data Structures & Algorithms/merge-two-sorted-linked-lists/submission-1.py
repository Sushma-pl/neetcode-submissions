# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node, newhead = None, None
        if list1 is None:
            return list2 
        
        if list2 is None:
            return list1 

        while list1 and list2:
            if newhead:
                if list1.val <= list2.val:
                    node.next = list1
                    list1 , node = list1.next, node.next
                else:
                    node.next = list2
                    list2 , node = list2.next, node.next
            else:
                if list1.val <= list2.val:
                    newhead, node = [list1, list1]
                    list1 = list1.next
                else:
                    newhead, node = [list2, list2] 
                    list2 = list2.next
        
        if list1:
            node.next = list1
        elif list2:
            node.next = list2 

        return newhead 

        