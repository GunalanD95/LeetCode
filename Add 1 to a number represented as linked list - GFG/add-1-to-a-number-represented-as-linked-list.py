#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self,head):
        prev = head
        cur  = head.next
        
        head.next = None
        
        while cur:
            # print(cur.data)
            cn = cur.next
            cur.next = prev
            prev = cur
            cur = cn
            
        return prev
        
    
    def addOne(self,head):
        #Returns new head of linked List.
        
        newHead = self.reverse(head)
        
        if newHead.data < 9:
            newHead.data += 1
            check = self.reverse(newHead)
            return check
            
        else:
            carry = 1
            current = newHead
            
            while current:
                new_val = current.data + carry
                
                if new_val > 9:
                    current.data = 0
                else:
                    current.data = new_val
                    carry = 0
                    
                current = current.next
            
            if carry:
                newNode = Node(1)
                newNode.next = newHead
                return newNode
            else:
                check = self.reverse(newHead)
                return check


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends