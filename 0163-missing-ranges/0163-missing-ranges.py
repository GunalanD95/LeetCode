class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        if not nums: return [[lower,upper]]
        if lower == upper: return []
        
        missing_ranges = []
        
        if nums[0] > lower:
            missing_ranges.append([lower, nums[0] - 1])
            
        
        for i in range(n-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            missing_ranges.append([nums[i]+1,nums[i+1]-1])
        
        
        if nums[-1] < upper:
            missing_ranges.append([nums[-1]+1,upper])
            
            
        return missing_ranges
        