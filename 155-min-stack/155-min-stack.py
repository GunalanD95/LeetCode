class Node():
    def __init__(self,val,next=None):
        self.val = val
        self.next = None
        
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.minhead = None
                        
    def insertfront(self,val):
        newNode = Node(val)
        if self.head:
            temp = self.head
            newNode.next = temp
            self.head = newNode
        else:
            self.head = newNode
        
        minnewNode = Node(val)
        if self.minhead == None:
            self.minhead = minnewNode
        
        elif self.minhead.val == None:
            self.minhead = minnewNode
            
        elif val <= self.minhead.val:
            oldmin = self.minhead
            minnewNode.next = oldmin
            self.minhead = minnewNode
            
    def pop(self):
        if self.head:
            remove = self.head
            if remove.val == self.minhead.val:
                oldmin = self.minhead
                self.minhead = oldmin.next               
            
            newhead = remove.next
            self.head = newhead
        else:
            return
        
    def top(self):
        if self.head:
            return self.head.val
        else:
            return 


class MinStack:

    def __init__(self):
        self.ll = LinkedList()
        

    def push(self, val: int) -> None:
        return self.ll.insertfront(val)
        

    def pop(self) -> None:
        return self.ll.pop()
        

    def top(self) -> int:
        return self.ll.top()
        

    def getMin(self) -> int:
        return self.ll.minhead.val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()