#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1]*(N+1) for i in range(N+1)]
        
        
        def getmeMatrix(i,j):
            if i == j:
                return 0
                
                
            if dp[i][j] != -1:
                return dp[i][j]
                
                
            min_val = float('inf')
            
            # loop from i to j -1
            for k in range(i,j):
                value = (arr[i-1] * arr[k] * arr[j]) + getmeMatrix(i,k) + getmeMatrix(k+1,j)
                min_val = min(min_val,value)
                
            dp[i][j] =   min_val  
            
            return dp[i][j]


        return getmeMatrix(1,N-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends