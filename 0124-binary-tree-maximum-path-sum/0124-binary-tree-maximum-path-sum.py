class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')
        
        def _dfs(node):
            if not node:
                return 0


            left  = _dfs(node.left)
            right = _dfs(node.right)

            left = max(left,0)
            right = max(right,0)
            self.max_val  = max(self.max_val ,left+node.val+right)

            return  node.val + max(left,right) 
        
        _dfs(root)
        
        return self.max_val