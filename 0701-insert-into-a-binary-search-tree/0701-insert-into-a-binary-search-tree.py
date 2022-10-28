# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        parent = None
        temp = root
        
        while temp:
            parent = temp
            
            if temp.val > val:
                temp = temp.left
                
            elif temp.val < val:
                temp = temp.right
                
        newNode = TreeNode(val)
        
        if not parent:
            parent = newNode
            return parent
        
        elif parent.val > val:
            parent.left  = newNode
            return root
            
        else:
            parent.right = newNode
            return root
        