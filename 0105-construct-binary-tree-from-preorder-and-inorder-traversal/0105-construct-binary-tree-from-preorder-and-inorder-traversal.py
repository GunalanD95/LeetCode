# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrMap = {}
        for i in range(len(inorder)):
            inOrMap[inorder[i]] = i
        
        
        return self.helper(0,0,len(inorder)-1,preorder,inorder,inOrMap)
        
        
    def helper(self,preStart,inStart,inEnd,preorder,inorder,inOrMap):
        if preStart > len(preorder) - 1 or inStart > inEnd:
            return None 
        
        root_node = TreeNode(preorder[preStart])
        root_indx = inOrMap.get(root_node.val)
        root_node.left = self.helper(preStart + 1,inStart,root_indx -1 ,preorder,inorder,inOrMap)
                
        root_node.right = self.helper(preStart + root_indx - inStart + 1,root_indx+1,inEnd,preorder,inorder,inOrMap)

        
        return root_node