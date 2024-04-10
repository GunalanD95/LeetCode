from collections import defaultdict

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth  = defaultdict(int)
        height = defaultdict(int)
        
        def dfs(node,level):
            nonlocal height 
            if not node: return -1
            depth[node.val]  = level
            height[node.val] = max(dfs(node.left,level+1),dfs(node.right,level+1)) + 1
            return height[node.val]
        
        dfs(root,0)
        
        cousins = defaultdict(list)
        
        for node , level in depth.items():
            cousins[level].append((-height[node], node))
            cousins[level].sort()
            if len(cousins[level]) > 2:
                cousins[level].pop()
                
        res = []
        
        for node in queries:
            level = depth[node]
            
            if len(cousins[level]) == 1:
                res.append(level - 1)
            elif cousins[level][0][1] == node:
                res.append(-cousins[level][1][0] + level)
            else:
                res.append(-cousins[level][0][0] + level)
        return res

        
        
        
        
        
        
        
        