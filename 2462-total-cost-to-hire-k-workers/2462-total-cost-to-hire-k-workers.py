class Solution:
    def totalCost(self, cst, k, c):
        
        n, res = len(cst), 0                           # to use just one heap, we have to be 
        pairs  = [(t, i) for i, t in enumerate(cst)]   # able to extract the origin of a number
        l, r   = min(c,n//2), max(n-c,n//2)            # (left/right) when popping from the heap,
        pq     = pairs[:l] + pairs[r:]                 # thus, we save index for each number
        
        heapify(pq)

        for _ in range(k):                             # the smallest number comes first; if there
            cost, i = heappop(pq)                      # are several such numbers then the one with
            if i < l  : i, l = l, l+1                  # the smallest index (from the left) is taken
            if i >= r : i, r = r-1, r-1                
            if l <= r : heappush(pq, pairs[i])         # push numbers until they are depleted
            res += cost
        
        return res