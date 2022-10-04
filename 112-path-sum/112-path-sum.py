# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        def dfs(node,cur_sum):
            if not node:
                return False

            cur_sum += node.val
             
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    return True
                else:
                    return False



            left = dfs(node.left,cur_sum)
                
            right = dfs(node.right,cur_sum) 
            
            if left == True or right == True:
                return True
            else:
                return False
                
                
            # return False
        
        
        
        return dfs(root,0)