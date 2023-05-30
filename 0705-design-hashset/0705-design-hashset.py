class ListNode:
    def __init__(self,val):
        self.val  = val
        self.next = None
        

class MyHashSet:

    def __init__(self):
        self.root = None
        

    def add(self, key: int) -> None:
        newNode   = ListNode(key)
        if not self.contains(key):
            if not self.root:
                self.root = newNode
            else:
                tempHead  = self.root
                newNode.next = tempHead
                self.root = newNode

    def remove(self, key: int) -> None:
        if self.contains(key):
            prev  = None
            temp  = self.root
            
            while temp:
                if temp.val == key:
                    break
                prev = temp
                temp = temp.next
            
            if prev:
                prev.next = temp.next
            else:
                self.root = temp.next
                    
        

    def contains(self, key: int) -> bool:
        temp = self.root
        while temp:
            if temp.val == key:
                return True
            temp = temp.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)