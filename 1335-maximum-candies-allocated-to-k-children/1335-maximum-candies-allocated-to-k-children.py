from typing import List

class Solution:
    def canDistribute(self, candies: List[int], k: int, mid: int) -> bool:
        count = sum(candy // mid for candy in candies)  # Count how many children can get `mid` candies
        return count >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:  # If total candies are less than children, each gets 0.
            return 0
        
        low, high = 1, max(candies)  # Start binary search from 1 to max(candies)
        max_count = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.canDistribute(candies, k, mid):
                max_count = mid  # Store the max valid `mid`
                low = mid + 1  # Try a larger value
            else:
                high = mid - 1  # Try a smaller value
        
        return max_count
