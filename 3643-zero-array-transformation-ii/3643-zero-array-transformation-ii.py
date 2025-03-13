from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        # **Edge Case: nums is already a zero array**
        if all(x == 0 for x in nums):
            return 0  # ✅ Already zero, no queries needed!

        def canZeroify(k):
            """Check if we can make nums all zeros using the first k queries."""
            temp_nums = nums[:]  # Copy original nums
            diff = [0] * (N + 1)  # Difference array
            
            # Apply first k queries using the difference array
            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                if r + 1 < N:
                    diff[r + 1] += val
            
            # Apply prefix sum to reconstruct nums
            decrement = 0
            for i in range(N):
                decrement += diff[i]
                temp_nums[i] += decrement  # Apply decrement from difference array
                
                if temp_nums[i] > 0:  # If still positive, we failed
                    return False
            
            return True  # Successfully made nums zero

        # Binary search for minimum k
        left, right = 1, len(queries)
        answer = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canZeroify(mid):
                answer = mid
                right = mid - 1  # Try smaller k
            else:
                left = mid + 1  # Increase k
        
        return answer
