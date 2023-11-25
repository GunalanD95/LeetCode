class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        N = len(nums)

        pf = [0] * N
        pf[0] = nums[0]

        for i in range(1,N):
            pf[i] = nums[i] + pf[i-1]

        ans = [0] * N 
        cur_sum = 0
        
        for k in range(N):
            LFS = 0 
            RFS = 0
            if k == 0:
                LFS = 0
                RFS = pf[N-1] - pf[k]
            else:
                LFS = pf[k-1]
                RFS = pf[N-1] - pf[k]

            lsum = ( k * nums[k] ) - LFS
            rsum = RFS - ( (N-k-1) * nums[k] )
            cur_sum = lsum + rsum 
            ans[k] = cur_sum
            
            
        return ans
        
        '''
        
        since the array is sorted we know the elements are < on left and vice versa
        
        so using this we can precompute the sum and use prefix sum to calculate 
        
        left sum and right sum .
        
        ie = (no of elements) * cur_element -  left_side_sum
                    +
             right_side_sum   - cur_element * (no of elements) 
        
        '''