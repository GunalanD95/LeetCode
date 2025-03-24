"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def find_level(self,node,arr):
        if not node:
            return 0
        arr.append(node)
        return self.find_level(node.parent,arr) + 1

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        first   = []
        p_level = self.find_level(p,first)
        second  = []
        q_level = self.find_level(q,second)

        idx   = len(first) -1
        idx_2 = len(second) -1

        last_root = None
        while idx >= 0 and idx_2 >= 0:
            if first[idx] == second[idx_2]:
                last_root = first[idx]
            else:
                break
            idx  -= 1
            idx_2 -= 1

        return last_root
