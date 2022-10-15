from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        ans = []
        
        q.append(root)
        
        while q:
            level = len(q)
            cur_level = []
            for i in range(level):
                cur_node = q.popleft()
                if cur_node:
                    cur_level.append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)
                
            if cur_level: 
                ans.append(cur_level)
            
            
            
        return ans 
        
        
        