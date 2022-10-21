# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def calheight(root):
            if not root:
                return 0

            left = calheight(root.left)
            right = calheight(root.right)
            
            self.ans = max(self.ans,left+right)

            return max(left,right) + 1
        
        
        calheight(root)
        
        return self.ans
                
            
            
        