from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        
        q = deque()
        q.append(root)
        ans = []
        
        while q:
            level = []
            for i in range(len(q)):
                cur_node = q.popleft()
                if cur_node:
                    q.append(cur_node.right)
                    q.append(cur_node.left)
                    
                    if len(level) == 0:
                        level.append(cur_node.val)



            # since we need 1st one in each level
            if level: 
                ans.append(level[0])
                
        return ans
                    
            