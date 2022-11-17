#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        self.res = []
        if m[0][0] == 0:
            return [-1]
            
        def check(ans,i,j,mat,N):
            if i < 0 or i >= N or  j < 0 or j >= N:
                return False
                
            if mat[i][j] == 0 or mat[i][j] == 2:
                return False

            if i == N-1 and j == N-1:
                self.res.append(ans)
                return 
        
            mat[i][j] = 2 # visited 
            
            check(ans + 'U',i-1,j,mat,N)
            check(ans + 'R',i,j+1,mat,N)
            check(ans + 'D',i+1,j,mat,N)
            check(ans + 'L',i,j-1,mat,N)
            
            mat[i][j] = 1
                   
        check('',0,0,m,n)
        if not self.res:
            return [-1]
        
        return self.res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends