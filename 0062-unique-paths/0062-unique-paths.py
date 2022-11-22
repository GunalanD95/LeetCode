from functools import lru_cache
from collections import defaultdict
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
            
        hashmap = defaultdict(set)
        
                
        def rateinMaze(i,j,hashmap):
            if i >= m or  j >=n:
                return 0 
            
            if i == m-1 and j == n-1:
                return 1
            
            if (i,j) not in hashmap:
                hashmap[(i,j)] = rateinMaze(i+1,j,hashmap) +  rateinMaze(i,j+1,hashmap)
            
            return hashmap[(i,j)]
                
        
        return(rateinMaze(0,0,hashmap))
        