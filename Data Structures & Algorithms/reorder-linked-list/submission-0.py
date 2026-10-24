# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return head

        slow = head
        fast = head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        # fist half: head to slow . we have first list always greater than second
        first = head
        second = slow.next 
        slow.next = None

        # reverse second half
        prev = None 
        node = second
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp 
        
        second = prev

        # merge two list
        while first and second:
            temp1 = first.next 
            temp2 = second.next

            first.next = second
            second.next = temp1
            first = temp1
            second = temp2 

        




