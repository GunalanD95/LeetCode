from collections import  deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        
        q = deque()
        q.append(root)
        
        
        ans = []
        lvl = 1
        while q:
            level = deque()
            for i in range(len(q)):
                cur_node = q.popleft()
                
                if cur_node:
                    if lvl & 1:
                        level.append(cur_node.val)
                    else:
                        level.appendleft(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)

            if level:
                ans.append(list(level))
            lvl += 1
            
        return ans 
        
                