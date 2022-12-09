from collections import *
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append( (root,root.val,root.val) )
        
        res = -1
        
        while q:
            
            for _ in range(len(q)):
                cur_node , min_val , max_val = q.popleft()
                
                value = abs(max_val - min_val)
                
                res = max(res,value)
                
                if cur_node.left:
                    q.append((cur_node.left,min(cur_node.left.val,min_val)                              ,max(cur_node.left.val,max_val) ) )
                    
                if cur_node.right:
                    q.append( (cur_node.right,min(cur_node.right.val,min_val),max(cur_node.right.val,max_val) ) )
                    
                    
                    
        return res 
        