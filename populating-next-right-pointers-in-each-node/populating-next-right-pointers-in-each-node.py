"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        q = deque()
        q.append(root)
        prev_node = None
        
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                
                if prev_node:
                    prev_node.next = cur_node
                
                    print("cur_node",cur_node.val,"prev_node",prev_node.val)
                if cur_node.left:
                    q.append(cur_node.left)

                if cur_node.right:
                    q.append(cur_node.right)
                prev_node = cur_node
            print("<->")
            prev_node.next = None
            prev_node = None
        
        
        return root
        