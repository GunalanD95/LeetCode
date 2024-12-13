"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = deque()
        q.append(root)
        while q:
            cur = []
            for _ in range(len(q)):
                cur_node = q.popleft()
                cur.append(cur_node.val)
                for child in cur_node.children:
                    q.append(child)

            if cur:
                res.append(cur[:])
            
        return res