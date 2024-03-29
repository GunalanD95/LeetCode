# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = []
        count = 0
        stack.append(root)
        
        while len(stack) != 0:
            node = stack.pop()
            count += 1
            if node.right: stack.append(node.right)
            if node.left:  stack.append(node.left)
                
        return count