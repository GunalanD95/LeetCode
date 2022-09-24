class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        stack = []
        cur_stack = []
        
        def dfs(node,cur_sum):
            if not node:
                return
        
            cur_sum += node.val
            cur_stack.append(node.val)
            
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    temp = cur_stack.copy()
                    stack.append(temp) 
                    
            left = dfs(node.left,cur_sum)
            right = dfs(node.right,cur_sum)
            
            cur_stack.pop()
            
                
                
        dfs(root,0)
        return stack
        