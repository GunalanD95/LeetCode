class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Helper function to calculate the maximum subarray sum using Kadane's algorithm
        def kadane_max(nums):
            cur_sum = 0
            ans = float('-inf')
            for num in nums:
                cur_sum += num
                ans = max(ans, cur_sum)
                if cur_sum < 0:
                    cur_sum = 0
            return ans
        
        # Helper function to calculate the minimum subarray sum
        def kadane_min(nums):
            cur_sum = 0
            ans = float('inf')
            for num in nums:
                cur_sum += num
                ans = min(ans, cur_sum)
                if cur_sum > 0:
                    cur_sum = 0
            return ans

        # Step 1: Compute the maximum subarray sum (non-circular case)
        max_kadane = kadane_max(nums)
        
        # Step 2: Compute the minimum subarray sum
        min_kadane = kadane_min(nums)
        
        # Step 3: Compute the total sum of the array
        total_sum = sum(nums)
        
        # Step 4: Handle the circular case and all-negative case
        # If all elements are negative, total_sum - min_kadane will be 0, so return max_kadane
        if total_sum == min_kadane:
            return max_kadane
        
        # Step 5: Compute the maximum sum as the max of non-circular and circular cases
        max_circular = total_sum - min_kadane
        return max(max_kadane, max_circular)
