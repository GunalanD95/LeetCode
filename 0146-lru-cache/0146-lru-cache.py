class Node:
    def __init__(self,key,val,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head  = Node(-1,-1)
        self.tail  = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addAtHead(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        

    def removeNode(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeNode(node)
        self.addAtHead(node)
        self.cache[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:
        newNode = Node(key,value)
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addAtHead(newNode) 
        elif self.size == self.capacity:
            node = self.tail.prev
            self.removeNode(node)
            self.addAtHead(newNode)
        else:
            self.addAtHead(newNode) 
            self.size += 1
        self.cache[key] = newNode
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)