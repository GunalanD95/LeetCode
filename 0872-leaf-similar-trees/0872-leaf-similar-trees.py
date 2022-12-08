class Solution:
    def _dfs(self,node,cur):
        if not node:
            return 

        if not node.left and not node.right:
            cur.append(node.val)


        self._dfs(node.left,cur)
        self._dfs(node.right,cur)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and root2: return False
        if not root2 and root1: return False
        
        list1 = []
        list2 = []
        
        self._dfs(root1,list1)
        self._dfs(root2,list2)
        
        if list1 != list2:
            return False
        return True 
        