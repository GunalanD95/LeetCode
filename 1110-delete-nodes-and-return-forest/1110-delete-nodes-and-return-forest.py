class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = []
        
        def dfs(node,is_root):    
            if not node:
                return
            
            if node.val in to_delete:
                dfs(node.left,True)
                dfs(node.right,True)
            else:
                if node.left:
                    if node.left.val in to_delete:
                        dfs(node.left,True)
                        node.left = None
                    else:
                        dfs(node.left,False)
                        
                if node.right:
                    if node.right.val in to_delete:
                        dfs(node.right,True)
                        node.right = None
                    else:
                        dfs(node.right,False) 
            if node.val not in to_delete and is_root:
                forest.append(node)

        dfs(root,True)
        return forest
        
        