"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        q = deque()
        q.append(node)
        
        clones = {node.val: Node(node.val,[])}
        
        while q:
            cur_node  = q.popleft()
            cur_clone = clones[cur_node.val]
            
            for child in cur_node.neighbors:
                cur_child = child.val
                
                if cur_child not in clones:
                    clones[cur_child] = Node(cur_child,[])
                    q.append(child)
                    
                cur_clone.neighbors.append(clones[cur_child])
                
        return clones[node.val]
        