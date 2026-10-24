# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        # to ensure that left pointer is just before node, that is going to be delted

        # make distance between head and second = n
        left = dummy
        k = 0
        second  = head
        while k < n:
            k+=1
            second = second.next 

        # left will point exactly before the node that is going to be deleted 
        while second:
            left = left.next
            second = second.next 
        
        left.next = left.next.next 

        return dummy.next  
        

