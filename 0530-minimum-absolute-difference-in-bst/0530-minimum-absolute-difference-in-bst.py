# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        self.prev = None
        
        def inorder(node):
            nonlocal min_diff
            if not node: return
            
            inorder(node.left)
            if self.prev != None:
                min_diff = min(min_diff,abs(node.val - self.prev))
            self.prev = node.val
            inorder(node.right)
            
        inorder(root)
        
        return min_diff