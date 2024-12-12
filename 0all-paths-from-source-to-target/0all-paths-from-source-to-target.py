class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        if not graph: return res
        N   = len(graph)
        q = deque()
        q.append((0,[0])) # (node,path)
        while q:
            for _ in range(len(q)):
                cur_node , cur_path  = q.popleft()
                
                if cur_node == N-1:
                    res.append(cur_path)
                    continue
                    
                for child in graph[cur_node]:
                    q.append((child,cur_path+[child]))
        
        
        return res