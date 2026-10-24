"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        node = head 
        newhead = Node(head.val)

        # inserting a new node between the the node in the first list
        while node:
            newnode = Node(node.val)
            newnode.next = node.next 
            node.next = newnode
            node = newnode.next 
        
        # while head:
        #     print(head.val)
        #     head = head.next 
        # copy random pointers
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            else:
                node.next.random = None
            node = node.next.next
        
        # making list: removing the newly created list
        newhead = head.next 
        node = head 
        while node:
            temp = node.next
            node.next = node.next.next
            if temp.next:
                temp.next = temp.next.next
            else:
                temp.next = None
            node = node.next
        
        return newhead
        # return None


