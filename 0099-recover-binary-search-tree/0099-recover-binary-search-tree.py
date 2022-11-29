class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        self.first = self.middle = self.last = None
        boolean = False
        self.prev    = None
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first   = self.prev 
                    self.middle  = node
                else:
                    boolean = True
                    self.last = node
            
            
            self.prev = node
            inorder(node.right)
            
            
        inorder(root)
        
        if self.first and self.last:
            temp = self.first.val
            self.first.val = self.last.val
            self.last.val =  temp 
            
        else:
            temp = self.first.val
            self.first.val = self.middle.val
            self.middle.val =  temp       
            
            
        return root
            
              
            
        