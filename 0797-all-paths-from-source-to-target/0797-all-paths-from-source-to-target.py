class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph: return []

        # build di-graph
        n     = len(graph)

        stack = [(0,[0])]      # - store noth the (node, and the path leading to it)

        res   = []

        while stack:
            cur_node , cur_path = stack.pop()
            
            if cur_node == n -1:
                res.append(cur_path)


            for child in graph[cur_node]:
                stack.append((child , cur_path + [child]))


        return res 



        