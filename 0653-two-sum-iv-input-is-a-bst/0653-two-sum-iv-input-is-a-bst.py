from collections import deque

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        q = deque()
        q.append(root)
        
        hmap = {}
        
        while q:
            cur_node = q.popleft()
            
            if cur_node.left:
                q.append(cur_node.left)
                
            if cur_node.right:
                q.append(cur_node.right)
                
            
            
            if (k - cur_node.val) in hmap:
                return True
            
            if cur_node.val not in hmap:
                hmap[cur_node.val] = 1
            else:
                hmap[cur_node.val] += 1
                
                
        return False
        