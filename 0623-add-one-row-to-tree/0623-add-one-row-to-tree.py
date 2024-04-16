from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        lvl = 1
        target_node = None
        
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                
                if lvl == depth -1:
                    temp_node1 = TreeNode(val)
                    temp_node2 = TreeNode(val)
                    
                    temp_node1.left  = cur_node.left
                    temp_node2.right = cur_node.right
                    
                    cur_node.left  = temp_node1
                    cur_node.right = temp_node2
                
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            if lvl == depth -1:
                break
            lvl += 1
         
        return root
        
        