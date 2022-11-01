class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return 
        self.count = 0
        self.val   = root
        def inordeTraversal(node):
            if not node:
                return
            
            inordeTraversal(node.left)
                
            self.count += 1
            if self.count == k:
                self.val = node.val
            
            inordeTraversal(node.right)
            
            
        inordeTraversal(root)
        
        return self.val

       