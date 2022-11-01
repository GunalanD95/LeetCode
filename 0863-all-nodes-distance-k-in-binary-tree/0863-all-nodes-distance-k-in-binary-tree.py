class Solution:
    def countNodes(self,node,k):
        nodes = []
        def _dfs(node,k):
            if not node:
                return 0

            if k == 0:
                nodes.append(node.val)

            x = _dfs(node.left,k-1)
            y = _dfs(node.right,k-1)

        _dfs(node,k)
        return nodes
    
    def pathtoNode(self,node,target):
        ans = []
        def dfs(node,k,stack):
            if not node:
                return
                
            stack.append(node)
            if node.val == k.val:
                temp = stack.copy()
                ans.extend(temp)
                    
            dfs(node.left,k,stack)
            dfs(node.right,k,stack)
            
            stack.pop()
            
        dfs(node,target,[])
        return ans
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root: return
        
        path = self.pathtoNode(root,target)
        
        # loop from back and reduce k - 1
        n = len(path)
        ans  = []
        ans.extend(self.countNodes(path[-1],k))
        prev = path[-1]
        
        for i in range(n-2,-1,-1):
            cur_node = path[i]
            k -= 1
            
            if k == 0:
                ans.append(cur_node.val)
                break
            
            if cur_node.left == prev:
                ans.extend(self.countNodes(cur_node.right,k-1))
            else:
                ans.extend(self.countNodes(cur_node.left,k-1))
                
            
                
            prev = cur_node
            
            
        return ans 
            
            
            
        
        