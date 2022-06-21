#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
        dic = {}
        A = nums
        for i in range(len(A)):
            if A[i] not in dic:
                dic[A[i]] = 1
            else:
                dic[A[i]] = 2

        res = []
        for j in dic:
            if dic[j] == 1:
                res.append(j)

        res.sort()
        return(res)
		    
		


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends