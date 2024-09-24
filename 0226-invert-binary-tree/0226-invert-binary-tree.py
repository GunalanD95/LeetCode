from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque()
        q.append(root)
        
        while q:
            cur_node = q.popleft()
            
            if cur_node:
                cur_node.left , cur_node.right = cur_node.right , cur_node.left
                q.append(cur_node.left)
                q.append(cur_node.right)
                
                
        return root
        