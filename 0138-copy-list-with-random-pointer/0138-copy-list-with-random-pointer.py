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
        if not head:
            return None
        
        hmap = defaultdict()
        new = Node(head.val)
        
        hmap[head] = new
        old  = head.next
        temp = new 
        
        
        while old:
            newNode = Node(old.val)
            hmap[old] = newNode
            
            temp.next = newNode
            temp = temp.next
            old  = old.next
        
        hmap[None] = None
        tme = new
        old = head
        while old:
            tme.random = hmap[old.random]
            tme = tme.next
            old = old.next
            
        return new