#User function Template for python3

class Solution:
    def countFriendsPairings(self, n):
        # code here 
        dp = [-1] * (n+1)
        dp[0] = 0
        if n > 0:
            dp[1] = 1
            
        if n > 1:
            dp[2] = 2
            
        for i in range(3,n+1):
            dp[i] = ( dp[i-1] % 1000000007 + (i-1) * dp[i-2] % 1000000007) % 1000000007
            
            
        return dp[n] % 1000000007
        


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