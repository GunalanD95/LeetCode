from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        # BFS 
        result = []
        
        
        queue = deque([(root, root.val, [root.val])])
        
        while queue:
            for i in range(len(queue)):
                cur_node , cur_sum , path = queue.popleft()
                
                if not cur_node.left and not cur_node.right:
                    if cur_sum == targetSum:
                        result.append(path)
                        
                
                if cur_node.left:
                    queue.append((cur_node.left, cur_sum + cur_node.left.val, path + [cur_node.left.val]))
                    
                    
                if cur_node.right:
                    queue.append((cur_node.right, cur_sum + cur_node.right.val, path + [cur_node.right.val]))
                    
        return result 