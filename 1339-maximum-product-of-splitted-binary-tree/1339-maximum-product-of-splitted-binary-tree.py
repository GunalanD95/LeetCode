    
class Solution:
    def _total_sum(self,node):
        if not node:
            return 0
        left  = self._total_sum(node.left)
        right = self._total_sum(node.right)
        total_sum = left + right + node.val 
        return total_sum 
    
    def _postorder(self,node,max_sum):
        if not node:
            return 0
        
        left  = self._postorder(node.left,max_sum)
        right = self._postorder(node.right,max_sum)
        
        cur_sum = left + right + node.val
        self.ans    = max(self.ans , (self.total_sum - cur_sum ) * cur_sum )
        return cur_sum 
        
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 1000000007
        self.total_sum = self._total_sum(root)
        self.ans       = 0
        self._postorder(root,0)
        return self.ans % MOD