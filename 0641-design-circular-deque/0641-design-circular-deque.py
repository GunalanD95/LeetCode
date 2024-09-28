class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev  = prev
        
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if not self.head:
            self.head = Node(value)
            self.tail = self.head 
        else:
            newHead = Node(value,self.head,None)
            self.head.prev = newHead
            self.head = newHead
        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if not self.head:
            self.head = Node(value)
            self.tail = self.head 
        else:
            newTail = Node(value,None,self.tail)
            self.tail.next = newTail
            self.tail = newTail
        self.size += 1
        return True        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
        
        
        self.size -= 1
        return True        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size ==  self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()