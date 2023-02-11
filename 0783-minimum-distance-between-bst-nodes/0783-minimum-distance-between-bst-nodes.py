# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        inorder = []
        
        min_diff = float('inf')
        
        def inorder_traversal(node):
            if not node:
                return
            
            inorder_traversal(node.left)
            inorder.append(node.val)
            inorder_traversal(node.right)
            
        
        inorder_traversal(root)
        
        print("inorder",inorder)
        for i in range(1,len(inorder)):
            value    = inorder[i] - inorder[i-1]
            min_diff = min(min_diff,value)
            
        return min_diff
            
            
        
            
            
        
        