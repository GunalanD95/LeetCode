# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque() 
        q.append(root)
        
        prev_lvl = True 
        while q:
            lvl = []
            for _ in range(len(q)):
                cur_node = q.popleft()
                if lvl and lvl[-1] == None and cur_node:
                    return False
                if cur_node:
                    if prev_lvl == False:
                        return False
                    lvl.append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)
                else:
                    lvl.append(None)
            if lvl[-1] == None:
                prev_lvl = False
            else:
                prev_lvl = True
        return True
        