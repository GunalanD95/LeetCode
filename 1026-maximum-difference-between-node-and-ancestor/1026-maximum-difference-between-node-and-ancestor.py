from collections import *
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append((root, root.val, root.val))
        answer = -math.inf
        
        while queue:
            
            queue_len = len(queue)
            for _ in range(queue_len):
                
                node, min_val, max_val = queue.popleft()
                diff1 = abs(node.val-min_val)
                diff2 = abs(node.val-max_val)
                
                answer = max(answer, diff1, diff2)
                
                if node.left:
                    queue.append((node.left, min(node.val, min_val), max(node.val, max_val)))
                    
                if node.right:
                    queue.append((node.right, min(node.val, min_val), max(node.val, max_val)))
                    
        return answer
        