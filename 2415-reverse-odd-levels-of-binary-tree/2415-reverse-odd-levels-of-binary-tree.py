from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = deque([root])
        level = 0  # Root level is 0 (even)
        
        while q:
            level_size = len(q)
            # Extract all node values in the current level if odd
            if level % 2 == 1:
                values = [node.val for node in q]
                for i, node in enumerate(q):
                    node.val = values[-(i + 1)]
            
            # Process the next level
            for _ in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return root
