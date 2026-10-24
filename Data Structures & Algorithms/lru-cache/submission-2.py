class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None 

class LRUCache:

    def __init__(self, capacity: int):
        self.dt = {}
        self.capacity  = capacity

        self.right, self.left = ListNode(0,0), ListNode(0,0)
        self.right.prev , self.left.next = self.left, self.right
    
    # remove from linked list 
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # insert into linked list 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.dt:
            self.remove(self.dt[key])
            self.insert(self.dt[key])
            return self.dt[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dt:
            self.remove(self.dt[key]) #remove fom ll
        
        self.dt[key] = ListNode(key,value)
        self.insert(self.dt[key])

        if len(self.dt) > self.capacity:
            lru  = self.left.next 

            # remove from ll
            self.remove(lru)

            # remove from hash
            del self.dt[lru.key]
            