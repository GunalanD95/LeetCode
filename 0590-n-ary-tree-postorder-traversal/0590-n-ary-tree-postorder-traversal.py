"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return 
        
        res = []
        stack1 , stack2 = [root] , []
        while stack1:
            cur_node = stack1.pop()
            res.append(cur_node.val)
            stack2.append(cur_node)

            if cur_node.children:
                stack1.append(cur_node.children.pop(0))
                
            while cur_node.children:
                stack1.append(cur_node.children.pop(0))

        return res[::-1]        