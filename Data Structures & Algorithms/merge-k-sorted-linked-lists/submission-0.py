# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        head = None
        newhead = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next 
        else:
            head = list2
            list2 = list2.next 

        newhead = head
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next 
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        while list1 :
            head.next = list1
            list1 = list1.next
            head = head.next
        
        while list2 :
            head.next = list2
            list2 = list2.next
            head = head.next

        return newhead


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n == 0:
            return None
        
        # if n == 1:
        #     return lists[0]

        head = lists[0]
        for i in range(1, n):
            head = self.mergeTwoLists(head, lists[i])
        
        return head


