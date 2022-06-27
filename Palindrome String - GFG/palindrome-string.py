#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		# code here
		temp = S
		S = list(S)
		def rev(A):
    		s = 0
    		e = len(A) - 1
    		while s <= e:
    		    tmp = A[s]
    		    A[s] =  A[e]
    		    A[e] = tmp
    		    s += 1
    		    e -= 1
            return A
            
        rev = rev(S)
        res = "".join(rev)
        if res == temp:
            return 1
        else:
            return 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends