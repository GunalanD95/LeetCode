# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def recpost(node):
            if not node: return
            
            if node.left: recpost(node.left)
                
            if node.right: recpost(node.right)
                
            res.append(node.val)
            
            
        recpost(root)
        
        return res
        