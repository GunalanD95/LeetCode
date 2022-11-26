#User function Template for python3

class Solution:
    def countFriendsPairings(self, n):
        # code here 
        mod = 1000000007
        dp = [-1] * (n+1)
        dp[0] = 0
        if n > 0:
            dp[1] = 1
            
        if n > 1:
            dp[2] = 2
            
        for i in range(3,n+1):
            dp[i] = ( dp[i-1] % mod + (i-1) * dp[i-2] % mod) % mod
            
            
        return dp[n] % mod
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countFriendsPairings(n))
# } Driver Code Ends