class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        else:
            c = 0
            temp = self.head
            while c < index:
                temp = temp.next
                c +=1
            return temp.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head:
            temp = self.head
            newNode.next = temp
            self.head = newNode
            self.length += 1
            
        else:
            self.head = newNode
            self.length += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.length += 1
        else:
            temp = self.head
            
            while temp.next:
                temp = temp.next
            temp.next = newNode
            self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
            
        else:
            newNode = Node(val)
            c = 0
            temp = self.head
            while c < index - 1:
                temp = temp.next
                c += 1
                
            newNode.next = temp.next
            temp.next = newNode
            self.length += 1 
                
            

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
    
        
        if index == 0:
            temp = self.head
            newhead = temp.next 
            self.head = newhead
            self.length -= 1  
            
        else:
            c = 0
            temp = self.head
            while c < index - 1:
                c += 1
                temp = temp.next
                
            
            temp.next = temp.next.next
            self.length -= 1 
                       


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)