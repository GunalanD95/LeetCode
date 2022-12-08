#User function Template for python3
from functools import lru_cache
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        N = len(arr)
        
        @lru_cache(None)
        def getMeMatrix(i,j):
            if i == j:
                return 0
                

            min_val = float('inf')
            
            # loop will run from i --> (j-1)
            for k in range(i,j):
                
                value = (arr[i-1] * arr[k] * arr[j]) + ( getMeMatrix(i,k) + getMeMatrix(k+1,j) )
                
                min_val = min(min_val,value)
 
                
            return min_val
            
        # print("getMeMatrix",getMeMatrix(1,N-1))
        return getMeMatrix(1,N-1)
                


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