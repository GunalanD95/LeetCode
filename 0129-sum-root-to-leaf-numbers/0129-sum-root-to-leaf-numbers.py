# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        def preorder(cur_sum,node):
            if not node:
                return 
            
            cur_sum = cur_sum * 10 + node.val
            
            if not node.left and not node.right:
                self.total_sum += cur_sum
                return 
            left  = preorder(cur_sum , node.left)
            right = preorder(cur_sum , node.right)
        preorder(0,root)
        return self.total_sum
        