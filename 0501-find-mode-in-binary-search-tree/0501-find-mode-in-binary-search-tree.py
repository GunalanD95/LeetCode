# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import *

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        hmap2 = defaultdict(int)
        max_count = 0
        def dfs(node):
            nonlocal max_count
            if not node:
                return
            
            dfs(node.left)
            hmap2[node.val] += 1
            max_count = max(max_count,hmap2[node.val])
            dfs(node.right)
            
        dfs(root)
        
        res = []
        
        for key in hmap2:
            if hmap2[key] == max_count:
                res.append(key)
        
        return res