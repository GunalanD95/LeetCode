class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        MOD = 10**9 + 7
        N = len(nums)
        low , high = 0 ,N-1
        ans = 0
        while low <= high:
            if nums[low] + nums[high] <= target:
                count = pow(2,high-low)
                ans   += count
                low +=1
            else:
                high -= 1
            
            
        return ans  % MOD
        