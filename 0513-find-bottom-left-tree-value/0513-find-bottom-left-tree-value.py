from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        
        
        levels = []
        while q:
            cur_level = []
            for _ in range(len(q)):
                cur_node = q.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            if cur_level:
                levels.append(cur_level)
                    
        
        return levels[-1][0]