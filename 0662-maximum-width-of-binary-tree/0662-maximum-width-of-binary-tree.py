# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        q = deque()
        q.append((root,0))
        
        res = 0
        while q:
            _ , level_start = q[0]
            _ , level_end   = q[-1]
            
            res = max(res, level_end - level_start + 1)
            
            for _ in range(len(q)):
                cur_node ,indx = q.popleft()
                    
                if cur_node.left:
                    q.append((cur_node.left,2*indx+1))
                if cur_node.right:
                    q.append((cur_node.right,2*indx+2))
            
        return res 