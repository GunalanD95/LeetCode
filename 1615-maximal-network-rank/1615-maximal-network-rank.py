class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        adj_list = collections.defaultdict(set)
        
        for u , v in roads:
            adj_list[u].add(v)
            adj_list[v].add(u)
            
        res = 0
        
        for city1,city2 in itertools.combinations(adj_list.keys(),2):
            has_connection = 1 if city1 in adj_list[city2] else 0
            
            total_sum = len(adj_list[city2]) + len(adj_list[city1])
            total_sum -= has_connection
            
            res = max(res,total_sum)
            
            
        return res
    
        '''
        TC : O(N)2
        SC : O(V+E)
        '''