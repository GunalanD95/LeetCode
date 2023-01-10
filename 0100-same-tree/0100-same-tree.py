# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def ide(A,B):
            if not A and not B:
                return 1
            
            if not A or not B:
                return 0
            
            
            if A.val != B.val:
                return 0 
            
            left = ide(A.left,B.left)
            right = ide(A.right,B.right)
            
            if left == 1 and right == 1:
                print("left",left,"right",right)
                return True
            else:
                print("else-l",left,"else-r",right)
                return False
            
            
        return ide(p,q)
        