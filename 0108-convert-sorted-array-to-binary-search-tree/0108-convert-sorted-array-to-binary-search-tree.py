# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        
        def dfs(arr,l,r):
            if l >= r:
                return None
            
            root_indx = (l+r)//2
            
            root = TreeNode(arr[root_indx])
            
            root.left = dfs(arr,l,root_indx)
            root.right = dfs(arr,root_indx+1,r)
            
            return root
        
        return dfs(nums,0,len(nums))
        