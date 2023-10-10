class Solution:
    def binarysearch(self, arr, low, target):
        high = len(arr) - 1
        idx = low
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                idx = mid
                low = mid + 1
            else:
                high = mid - 1
        return idx
    
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        nums = list(set(nums))
        nums.sort()
        
        min_operations = float('inf')
        for idx, num in enumerate(nums):
            # For each index, find the maximum value needed to make it continuous.
            elements_range = num + (N - 1)
            
            right_index = self.binarysearch(nums, idx, elements_range)
            
            # Calculate the number of operations required to make this subrange continuous.
            operations_needed = N - (right_index - idx + 1)
            
            min_operations = min(min_operations, operations_needed)
        
        return min_operations