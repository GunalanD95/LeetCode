class Solution:
    def checkLeafNode(self,node):
        if not node.left and not node.right:
            return 0
        
        elif not node.left or not node.right:
            return 1
        
        else:
            return 2 
        
        
        
    def SearchNode(self,node,key):
        parent = node 
        temp   = node
        
        while temp:
            if temp.val > key:
                parent = temp 
                temp = temp.left
                
            elif temp.val < key:
                parent = temp 
                temp = temp.right
            
            else:
                return parent , temp
             
            
                
        return None , None
        
    
    def findMin(self,parent,node):
        min_par  = parent
        min_node = node
        
        while min_node.left:
            min_par  = min_node
            min_node = min_node.left
            
        return min_par, min_node
    
    
    def deleteUtl(self,parent,delete_node):
        if parent.right == delete_node:
            parent.right = delete_node.right

            if delete_node.left:
                parent.right = delete_node.left

        elif parent.left == delete_node:
            parent.left  =  delete_node.right

            if delete_node.left:
                parent.left = delete_node.left
    
                
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.left and not root.right:
                return None
            
            if not root.left and root.right:
                root = root.right
                return root
               
            if not root.right and root.left:
                root = root .left
                return root            
            
        parent ,delete_node      = self.SearchNode(root,key)
        
        if not parent and not delete_node:
            return root 
        
        check_type               = self.checkLeafNode(delete_node)
        
        # print("parent_node",parent,"check_type",check_type)
        
        # Delete Node with 1 or ZERO CHILD
        
#         if delete_node == parent:
#             if check_type == 1:
#                 if parent.left:
#                     root = parent.left
#                 elif parent.right:
#                     root = parent.right
                
#                 return root
                
        
        
        if check_type == 0 or check_type == 1:
            self.deleteUtl(parent,delete_node)
            return root
            
        elif check_type == 2:
            rep_p , rep = self.findMin(delete_node,delete_node.right)
            self.deleteUtl(rep_p,rep)
            delete_node.val = rep.val
            return root