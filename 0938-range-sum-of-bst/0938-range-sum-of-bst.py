# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            total_sum = 0 
            if not node:
                return total_sum
            
            
            if node.val >= low and node.val <= high:
                total_sum += node.val
                
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            total_sum += left
            total_sum += right
            
            return total_sum
            
            
            
        
        
        
        return dfs(root)
            
        