# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTreeMap = defaultdict(list)
        
        res = []
        
        def preorder(node):
            if not node:
                return 'null'
            
            left  = preorder(node.left)
            right = preorder(node.right)
            
            cur_string = str(node.val) + ',' + left + ',' + right
            if len(subTreeMap[cur_string]) == 1:
                res.append(node)
            subTreeMap[cur_string].append(node)
            
            
            return cur_string
            
            
            
        print(preorder(root))
        return res
        