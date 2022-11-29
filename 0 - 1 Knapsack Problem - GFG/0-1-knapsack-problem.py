#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        hashmap = defaultdict(set)
        
        def dpKnapSack(indx,bag_weight):
            if bag_weight == 0:
                return 0
                
            if indx < 0:
                return 0
                
            if (indx,bag_weight) in hashmap:
                return hashmap[(indx,bag_weight)]
                
            
            take_it = float('-inf')
            if wt[indx] > bag_weight:
                dont_take = 0 + dpKnapSack(indx-1, bag_weight)
            else:
                dont_take = 0 + dpKnapSack(indx-1,bag_weight )
                take_it   = val[indx] + dpKnapSack(indx-1, bag_weight - wt[indx])
                
            hashmap[(indx,bag_weight)] = max(take_it,dont_take)
            
            return hashmap[(indx,bag_weight)]
            
            
        return dpKnapSack(n-1,W)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends