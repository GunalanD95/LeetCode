from collections import deque

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        q = deque()
        q.append((root, ""))
        
        while q:
            
            for i in range(len(q)):
                cur_node , ls = q.popleft()
                
                if not cur_node.left and  not cur_node.right:
                    ans.append(ls + str(cur_node.val) )
                    
                if cur_node.left:
                    q.append((cur_node.left,ls  + str(cur_node.val) + '->' ))
                    
                if cur_node.right:
                    q.append((cur_node.right,ls + str(cur_node.val) + '->' ))
                    
                    
        return ans
        
        
        