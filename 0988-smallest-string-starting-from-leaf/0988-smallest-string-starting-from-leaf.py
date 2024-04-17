# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        min_char = '{'
        def dfs(node,cur_arr):
            nonlocal min_char
            if not node:
                return
            cur_char = chr(node.val + ord('a'))
            if not node.left and not node.right:
                cur_arr = [cur_char] + cur_arr
                cur_str = "".join(cur_arr)
                if cur_str < min_char:
                    min_char = cur_str
            left  = dfs(node.left,[cur_char] + cur_arr)
            right = dfs(node.right,[cur_char] + cur_arr)
        dfs(root,[])        
        return min_char        