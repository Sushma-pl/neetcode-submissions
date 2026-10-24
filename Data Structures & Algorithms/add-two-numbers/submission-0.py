# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2

        if l2 is None:
            return l1 
        
        carry = 0
        prev = None
        dummy = ListNode(0)
        node = dummy 
        while l1 and l2:
            temp = l1.val + l2.val + carry
            node.next = ListNode(temp%10)
            carry = temp//10
            prev = l1
            l1 = l1.next
            l2 = l2.next
            node = node.next
        
        if l2:
            l1 = l2

        while l1:
            temp = l1.val  + carry
            node.next = ListNode(temp%10)
            carry = temp//10
            l1 = l1.next
            node = node.next
        
        
        while carry != 0:
            node.next = ListNode(carry%10)
            carry = carry//10
            node = node.next
        
        return dummy.next 
        
        