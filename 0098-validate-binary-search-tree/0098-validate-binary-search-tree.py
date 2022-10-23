# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,minval,maxval):
            if not node:
                return True
            
            if not (node.val > minval and node.val < maxval):
                print("yes",node.val,minval,maxval)
                return False
                
            left  = dfs(node.left,minval,node.val)
            
            right = dfs(node.right,node.val,maxval)
            
            if left and right:
                return True
            
            return False
            
        
            
            
        min_val = float('-inf')
        max_val = float('inf')
        
        
        return dfs(root,min_val,max_val)

        
                
            
        
        