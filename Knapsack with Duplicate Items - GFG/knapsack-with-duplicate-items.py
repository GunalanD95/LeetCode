#User function Template for python3
class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [[-1]*(W+1) for i in range(N+1)]
        
        for indx in range(N+1):
            for weight in range(W+1):
                dont_take = dp[indx-1][weight]
                
                if indx == 0 or wt == 0:
                    dp[indx][weight] = 0
                    
                elif wt[indx - 1] > weight:
                    dp[indx][weight] = dont_take
                
                else:
                    take_it  = val[indx-1] + dp[indx][weight - wt[indx - 1]]
                    dp[indx][weight] = max(dont_take,take_it)
                     
                    
        return (dp[N][W])


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