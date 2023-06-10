#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, N):
        # code here 
        ORG = N
        total_sum = 0
        while N != 0:
            last_digit = N % 10
            total_sum += (last_digit * last_digit * last_digit) 
            N = N // 10
        if total_sum == ORG:
            return "Yes"
        return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends