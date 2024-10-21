class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        visited = set()
        N = len(s)
        
        max_score = 0
        def find_all(indx):
            nonlocal max_score
            if indx >= N:
                print("max_score",len(visited),visited)
                max_score = max(max_score,len(visited))
                return

            for i in range(indx,N):
                cur_string = s[indx:i+1]
                if cur_string not in visited:
                    visited.add(cur_string)
                    find_all(i+1)
                    visited.remove(cur_string)
                    
        find_all(0)
        return max_score
        
        