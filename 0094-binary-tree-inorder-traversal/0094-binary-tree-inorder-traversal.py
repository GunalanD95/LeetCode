

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out_put = []
        
        stack = []

        cur_node = root
        
        while cur_node or stack:
            # go extreme left
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
                
            cur_node = stack.pop()
            out_put.append(cur_node.val)
            cur_node = cur_node.right
            
            
        return out_put
        
        