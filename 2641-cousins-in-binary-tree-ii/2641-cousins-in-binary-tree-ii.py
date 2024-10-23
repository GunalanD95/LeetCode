# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 0
        
        
        q = deque()
        q.append((root,None))
        
        levl = 1
        while q:
            cur_sum = defaultdict(int)
            
            cur_nodes = []
            for _ in range(len(q)):
                node, parent= q.popleft()
                cur_nodes.append((node,parent))
                if parent:
                    cur_sum[parent] += node.val
                
                if node.left:
                    q.append((node.left,node))
                    
                if node.right:
                    q.append((node.right,node))
                
            # print(levl,cur_sum,cur_nodes)
            for node,parent in cur_nodes:
                print(node.val, sum(cur_sum.values()) - cur_sum[parent])
                node.val = sum(cur_sum.values()) - cur_sum[parent]
            levl += 1
            
            
            
        return root
            
            
            