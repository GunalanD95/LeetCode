#User function Template for python3
class Solution:
	def minOperations(self, string1, string2):
		# code here
        cache   = {}
        def LCS(indx1,indx2):
            if indx1 >= len(string1) or indx2 >= len(string2):
                return abs(len(string1) - indx1) + abs(len(string2) - indx2)
            
            if (indx1,indx2) in cache:
                return cache[(indx1,indx2)]
            
            # if matched 
            if string1[indx1] == string2[indx2]:
                cache[(indx1,indx2)] = LCS(indx1+1,indx2+1)
            else:
                cache[(indx1,indx2)] =  min(1 + LCS(indx1+1,indx2),
                1 + LCS(indx1,indx2+1))
                
            return cache[(indx1,indx2)]
                
        return LCS(0,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends