from collections import defaultdict
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        self.max_diameter = 0
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            
        def find_diameter(node,parent):
            longest = 0
            second = 0
            
            for child in graph[node]:
                if child != parent:
                    child_count = find_diameter(child,node)
            
                    print(child,"child-count",child_count)
                
                    if child_count > longest:
                        second = longest
                        longest = child_count
                    elif child_count > second:
                        second = child_count
                        
                        
            print("node",node,"len",)
            self.max_diameter = max(longest+second,self.max_diameter)
            return longest + 1
        
        find_diameter(0,-1)
        return self.max_diameter