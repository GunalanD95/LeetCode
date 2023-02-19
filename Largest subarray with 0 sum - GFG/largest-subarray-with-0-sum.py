#Your task is to complete this function
#Your should return the required output
from collections import *
class Solution:
    def maxLen(self, n, arr):
        #Code here
        max_len = 0
        n   = len(arr)
        
        pf    = [0] * n
        pf[0] = arr[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + arr[i]
        
        hmap = defaultdict(int)
        hmap[0] = -1
        for i in range(n):
            num = pf[i]
            if num in hmap:
                cur_len = i - hmap[num] 
                max_len = max(cur_len,max_len)
            else:
                hmap[num] = i
            
            
        return max_len
            
        

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends