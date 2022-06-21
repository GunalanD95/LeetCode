#User function Template for python3
class Solution:
	def setBits(self, N):
		# code here
		c = 0
		for i in range(31):
		    mask = 1 << i
		    if mask & N:
		        c += 1
		return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends