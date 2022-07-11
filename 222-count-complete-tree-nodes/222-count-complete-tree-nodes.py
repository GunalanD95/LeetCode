# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = []
        
        def preorder(root):
            if root is None:
                return
            stack.append(root.val)
            
            if root.left: 
                preorder(root.left)
            if root.right: 
                preorder(root.right)
                
        preorder(root)
        
        return len(stack)
        