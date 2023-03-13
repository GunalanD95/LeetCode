# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checksym(A,B):
            if not A and not B:
                return 1
            
            if not A or not B:
                return 0
            
            if A.val != B.val:
                return 0
            
            left = checksym(A.left,B.right)
            
            right = checksym(A.right,B.left)
            
            
            if left == 1 and right == 1:
                return True
            else:
                return False
            
            
        return checksym(root,root)
        