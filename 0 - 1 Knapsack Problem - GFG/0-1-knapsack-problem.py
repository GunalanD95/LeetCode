#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[-1]*(W+1) for i in range(n+1)]
        
        for indx in range(n+1):
            for weight in range(W+1):
                dont_take = dp[indx-1][weight]
                
                if indx == 0 or wt == 0:
                    dp[indx][weight] = 0
                    
                elif wt[indx - 1] > weight:
                    dp[indx][weight] = dont_take
                
                else:
                    take_it  = val[indx-1] + dp[indx-1][weight - wt[indx - 1]]
                    dp[indx][weight] = max(dont_take,take_it)
                     
                    
        return (dp[n][W])


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