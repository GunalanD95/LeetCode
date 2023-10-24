# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        
        ans = []
        q = deque()
        q.append(root)
        
        while q:
            max_val = float('-inf')
            
            for _  in range(len(q)):
                cur_node = q.popleft()
                
                if cur_node.left:
                    q.append(cur_node.left)
                    
                if cur_node.right:
                    q.append(cur_node.right)
                    
                max_val = max(max_val,cur_node.val)
                
            if max_val != float('-inf'):
                ans.append(max_val)
                
                
        return ans