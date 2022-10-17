# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        global root_index 
        root_index = len(postorder) -1
        
        inOrdMap = {}
        for i in range(len(inorder)):
            inOrdMap[inorder[i]] = i
            
        
        return self.helper(0,len(inorder) -1 ,postorder,inorder,inOrdMap)
    
    
    
    
    def helper(self,inStart,inEnd,postorder,inorder,inOrdMap):
        global root_index
        if inStart > inEnd:
            return None 
        
        print("root_index",root_index)
        root = TreeNode(postorder[root_index])
        root_index -= 1
        
        root_indx = inOrdMap.get(root.val)
        
        root.right = self.helper(root_indx + 1 ,inEnd ,postorder,inorder,inOrdMap)
        root.left = self.helper(inStart,root_indx - 1 ,postorder,inorder,inOrdMap)
        
        
        
        return root 