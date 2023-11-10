from collections import *

class Solution:
    
    def get_all_nodes(self,graph,src_node):
        seen = set()
        seen.add(src_node)
        
        ans  = []
        
        q    = deque()
        q.append(src_node)
        
        
        while q:
            cur_node = q.popleft()
            
            ans.append(cur_node)
            
            for child in graph[cur_node]:
                if child not in seen:
                    seen.add(child)
                    q.append(child)
        
        return ans
        
        
    
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph    = defaultdict(list)
        min_len  = 1
        for u , v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        # not get the smallest value
        node_to_start = None
        for child in graph:
            if len(graph[child]) <= min_len:
                node_to_start = child
                min_len = min(min_len,len(graph[child]))
        
        ans =  self.get_all_nodes(graph,node_to_start)
        
        return ans