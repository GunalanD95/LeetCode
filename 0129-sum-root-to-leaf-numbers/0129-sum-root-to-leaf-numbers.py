# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        def preorder(cur_string,node):
            if not node:
                return ''
            if not node.left and not node.right:
                cur_string = cur_string + str(node.val)
                self.total_sum += int(cur_string)
                return 
            left  = preorder(cur_string + str(node.val) , node.left)
            right = preorder(cur_string + str(node.val)  , node.right)
        preorder('',root)
        return self.total_sum
        