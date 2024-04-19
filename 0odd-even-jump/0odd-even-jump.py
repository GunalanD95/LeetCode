"""

REF  : https://www.youtube.com/watch?v=oH7g5GLHWeU

"""
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)
        
        # find the next odd jump indx
        stack = []
        next_odd_jump = [0] * N
        for index,val in sorted(enumerate(arr),key=lambda x: x[1]):
            while stack and stack[-1] < index:
                next_odd_jump[stack.pop()] =  index
            stack.append(index)
        
        stack = []
        # find the next even jump indx
        next_even_jump = [0] * N
        for index,val in sorted(enumerate(arr),key=lambda x: x[1],reverse=True):
            while stack and stack[-1] < index:
                next_even_jump[stack.pop()] =  index
            stack.append(index)        

        # start from back -> odd start good and even start good
        odd_start_good  = [0] * N
        even_start_good = [0] * N
        
        # base case always can reach the last index
        odd_start_good[N-1] , even_start_good[N-1] = 1,1
        
        for i in range(N-2,-1,-1):
            i_next_odd = next_odd_jump[i]
            if i_next_odd and even_start_good[i_next_odd]:
                odd_start_good[i] = 1
                
            i_next_even = next_even_jump[i]
            if i_next_even and odd_start_good[i_next_even]:
                even_start_good[i] = 1        

        # return sum of odd start good = result
        return sum(odd_start_good)
        