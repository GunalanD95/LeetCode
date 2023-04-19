# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def computeZigZagHeight(self, node, direction):
        if not node:
            return 0 
        
        left = self.computeZigZagHeight(node.left, 'right')
        right = self.computeZigZagHeight(node.right, 'left')
            
        cur_len = max(left, right)
        self.max_path_len = max(self.max_path_len, cur_len)
        
        if direction == 'left':
            return left + 1
        elif direction == 'right':
            return right + 1
        else:
            return max(left, right) + 1
        
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_path_len = 0
        self.computeZigZagHeight(root,'')
        
        return self.max_path_len