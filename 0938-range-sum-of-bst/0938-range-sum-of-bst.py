# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total_sum = 0
        
        
        def _dfs(node):
            
            if not node:
                return 
            
            if node.val >= low and node.val <= high:
                print(node.val)
                self.total_sum += node.val
                
            print(self.total_sum)
                
            _dfs(node.left)
            _dfs(node.right)
            
        _dfs(root)
        return self.total_sum
        