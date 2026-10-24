# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverselist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        tail = None 

        while node:
            temp = node.next 
            node.next = prev 
            
            if prev is None:
                tail = node

            prev = node
            node = temp
        
        return prev, tail  #head and tail


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # for tranversing the lll\
        node = head

        count = 1
        curhead = head 

        newhead, newtail = None, None
        dummy = tail = ListNode() #store the new head 

        while node:
            if count %k == 0:
                # print(curhead.val ,node.val)
                
                count = 1 
                temp = node.next #head of next grp
                node.next = None

                newhead, newtail = self.reverselist(curhead)
                tail.next = newhead
                tail = newtail


                curhead = temp
                node = curhead
            else:
                count += 1
                node = node.next 
        
        #if length is not multiple of k 

        if count > 1:
            tail.next = curhead

        return dummy.next

            

