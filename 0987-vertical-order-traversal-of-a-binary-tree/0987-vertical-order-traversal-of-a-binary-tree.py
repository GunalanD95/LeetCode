from collections import deque , defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        d = defaultdict(list) # vertical:[level, node]
        q = deque()
        q.append((root, 0, 0)) # node, vertical, level
        
        min_val = float('inf')
        max_val = float('-inf')
        while q:
            node, vertical, level = q.popleft()
            d[vertical].append((level, node.val))
            
            if node.left:
                q.append((node.left,vertical-1,level+1))
                
            if node.right:
                q.append((node.right,vertical+1,level+1))
                        
                min_val = min(min_val,vertical)
                max_val = max(max_val,vertical)
                    
                    
        res = []
        for item in sorted(d):
            ans = []
            for i in sorted(d[item]):
                ans.append(i[1])
            res.append(ans)
        return res
            
            
        
        
        
        
        
        