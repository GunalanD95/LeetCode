# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cumulative_sum = 0
        def inorder(node):
            if not node:
                return
            
            right = inorder(node.right)
            self.cumulative_sum += node.val
            node.val = self.cumulative_sum
            left  = inorder(node.left)
        
        
        
        inorder(root)
        return root
        