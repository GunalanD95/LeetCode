# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        
        def preorder(root,low,high):
            if not root: return
            
            if root.val >= low and root.val <= high: self.ans += root.val
                
            if root.left: preorder(root.left,low,high)
                
            if root.right: preorder(root.right,low,high)
            
            
        preorder(root,low,high)
        
        return self.ans
            
        