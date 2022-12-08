# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def _dfs(node,cur):
            if not node:
                return 
            
            if not node.left and not node.right:
                cur.append(node.val)
                
            
            _dfs(node.left,cur)
            _dfs(node.right,cur)
            
            
        list1 = []
        list2 = []
        
        _dfs(root1,list1)
        _dfs(root2,list2)
        
        if list1 != list2:
            return False
        return True 
        