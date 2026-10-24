# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n the end = total-n+1 th from begining
        if head is None:
            return head 
        
        total = 0 
        node = head 
        while node:
            node = node.next 
            total +=1 
        
        # print(total)
        # from start 
        k = total - n + 1

        if k == 1:
            return head.next 

        count = 1 
        node = head 
        prev = None 

        while count < k:
            prev = node
            node = node.next 
            count +=1
       
        # remove the kth node from begining
        # print(node.val,node.next.val, prev.val) 
        prev.next = node.next 

        return head 

