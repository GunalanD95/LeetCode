#User function Template for python3
from collections import defaultdict
import sys 
sys.setrecursionlimit(10**6)

class Solution:
    def knapSack(self, N, W, val, wt):
        hashmap = defaultdict(set)
        
        def dpKnapSack(indx,bag_weight):
            if bag_weight <= 0:
                return 0
                
            if indx < 0:
                return 0
                
            if (indx,bag_weight) in hashmap:
                return hashmap[(indx,bag_weight)]
                
            
            take_it = -1000000000
            
            if wt[indx] > bag_weight:
                dont_take = dpKnapSack(indx-1, bag_weight)
            else:
                dont_take = dpKnapSack(indx-1,bag_weight )
                
                take_it   = val[indx] + dpKnapSack(indx, bag_weight - wt[indx])
                
            hashmap[(indx,bag_weight)] = max(take_it,dont_take)
            
            return hashmap[(indx,bag_weight)]
            
            
        return dpKnapSack(N-1,W)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends