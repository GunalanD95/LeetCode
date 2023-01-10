class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N       = len(A)
        max_len = float('-inf')

        for i in range(1,N-1):
            cur_indx = i
            if A[i + 1] < A[i] > A[i - 1]:
                left = i
                while left > 0 and A[left] > A[left -1]:
                    left -= 1
                        
                right = i
                while right+1 < N and A[right] > A[right+1]:
                    right +=1  
                cur_len = right - left + 1
                max_len = max(max_len,cur_len)
                
                
        if max_len != float('-inf'):
            return max_len
        else:
            return 0