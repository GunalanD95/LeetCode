#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        nums = A
        me = nums[0]
        c = 0
        
        for i in nums:
            if c == 0:
                me = i
                
            if i == me:
                c += 1
                
            elif i != me:
                c -= 1
                
        cc = 0
        for j in nums:
            if j == me:
                cc += 1   
        if cc > len(nums)/2:
            return me
        else:
            return -1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends