# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        low = 0
        high = mountain_arr.length() - 1
        peak = -1

        # Find the peak element
        while low < high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
            peak = low  # Peak element

        # Search in the left side of the mountain (increasing subarray)
        low = 0
        high = peak
        while low <= high:
            mid = (low + high) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1

        # Search in the right side of the mountain (decreasing subarray)
        low = peak
        high = mountain_arr.length() - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                high = mid - 1
            else:
                low = mid + 1

        return -1  # Target not found        