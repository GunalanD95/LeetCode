class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        N = len(s)
        
        min_insertions = float('inf')
        
        @cache
        def find_min_insertions(indx,left,right,insertions):
            nonlocal min_insertions
            if indx >= N:
                rems = abs(left - right)
                min_insertions =  min(min_insertions,rems+insertions)
                return
            
            
            if s[indx] == '(':
                left += 1
            else:
                right += 1
            
            if left >= right:
                return find_min_insertions(indx+1,left,right,insertions)
            else:
                return find_min_insertions(indx+1,right,right,insertions+1)
        

        find_min_insertions(0,0,0,0)
        
        return min_insertions