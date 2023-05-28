class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # sorting -> to make sure cuts are in ordered when paritioning 
        
        cuts.sort()
        
        cuts = [0] + cuts
        cuts.append(n)
        
        length = len(cuts)
        
        @cache
        def findoptimalcuts(start, end):
            if start == end - 1:
                return 0
            
            if start >= end:
                return 0
            
            min_cuts = float('inf')
            
            for indx in range(start + 1, end):
                cur_cut = cuts[end] - cuts[start]
                
                # consider cur_cut as mid point
                left_cut = findoptimalcuts(start, indx)
                right_cut = findoptimalcuts(indx, end)
                
                cur_cut += left_cut + right_cut
                
                min_cuts = min(min_cuts, cur_cut)
                
            return min_cuts
        
        return findoptimalcuts(0, length - 1)
